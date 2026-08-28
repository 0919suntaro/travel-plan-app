import streamlit as st

import config
import demo_data
import gemini_client
import storage
from schemas import (
    DestinationSuggestionList,
    MountainSuggestionList,
    PackingListResponse,
    TouristSpotList,
    TripPlan,
)
from layout import bento_rows
from theme import inject_theme, render_hero

st.set_page_config(page_title="旅行・登山 おすすめナビ", page_icon="🌲", layout="wide")
inject_theme()

REGIONS = [
    "指定なし",
    "北海道",
    "東北",
    "関東",
    "中部",
    "近畿",
    "中国",
    "四国",
    "九州・沖縄",
    "海外",
]

INTERESTS = [
    "自然・絶景",
    "歴史・文化",
    "グルメ",
    "温泉",
    "アクティビティ・体験",
    "アート・美術館",
    "子供連れ向け",
    "写真映え",
    "のんびり・癒し",
]

DIFFICULTIES = ["初級", "中級", "上級"]


def call_gemini(prompt: str, schema):
    if not config.GEMINI_API_KEY:
        st.error("サイドバーからGemini APIキーを設定するか、デモモードを有効にしてください。")
        return None
    try:
        with st.spinner("Geminiが考え中です..."):
            return gemini_client.generate_structured(prompt, schema)
    except Exception as e:  # noqa: BLE001 - surface any API/parse error to the user
        st.error(f"エラーが発生しました: {e}")
        return None


def call_ai(prompt: str, schema, demo_fn):
    """Run against Gemini, or return canned sample data when demo mode is on."""
    if st.session_state.get("demo_mode"):
        return demo_fn()
    return call_gemini(prompt, schema)


def favorite_button(kind: str, title: str, detail: dict, key: str) -> None:
    if st.button("⭐ お気に入りに追加", key=key):
        storage.add_favorite(kind, title, detail)
        st.toast(f"「{title}」をお気に入りに追加しました", icon="⭐")


# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------
with st.sidebar:
    st.header("⚙️ 設定")
    if not config.GEMINI_API_KEY:
        key_input = st.text_input(
            "Gemini API Key",
            type="password",
            help="環境変数 GEMINI_API_KEY または .env ファイルでも設定できます",
        )
        if key_input:
            config.GEMINI_API_KEY = key_input
            gemini_client.reset_client()
            st.session_state["demo_mode"] = False
            st.rerun()
    else:
        st.success("✅ APIキー設定済み")

    st.checkbox(
        "🎬 デモモード(サンプルデータ・APIキー不要)",
        value=not bool(config.GEMINI_API_KEY),
        key="demo_mode",
        help="オンにするとGeminiを呼ばず、あらかじめ用意したサンプルデータで全機能を試せます。",
    )
    if st.session_state.get("demo_mode"):
        st.info("🎬 デモモード中: 表示される内容はサンプルデータです。")

    st.caption(f"使用モデル: `{config.GEMINI_MODEL}`")
    st.divider()
    st.metric("⭐ お気に入り件数", len(storage.load_favorites()))
    st.caption("すべてローカルに保存され、外部には送信されません。")

render_hero()
st.caption("観光地・旅行プラン・山選びをGeminiがまとめてサポートする個人用ツールです。")

tabs = st.tabs(
    [
        "🏙️ 観光スポット検索",
        "🧭 雰囲気マッチプランナー",
        "⛰️ 山さがし",
        "🗓️ 旅行プラン自動生成",
        "🎒 持ち物リスト",
        "⭐ お気に入り",
    ]
)

# ---------------------------------------------------------------------------
# Tab 1: Tourist spot finder
# ---------------------------------------------------------------------------
with tabs[0]:
    st.subheader("観光地を入力すると、おすすめスポットを提案します")
    with st.form("spot_form"):
        place = st.text_input("観光地・都市名", placeholder="例: 京都, 金沢, ハワイ")
        interests = st.multiselect("興味のあるジャンル(任意)", INTERESTS)
        count = st.slider("提案してほしいスポット数", 3, 10, 5)
        submitted = st.form_submit_button("スポットを検索する", type="primary")

    if submitted:
        if not place.strip():
            st.warning("観光地・都市名を入力してください。")
        else:
            interest_text = "、".join(interests) if interests else "指定なし"
            prompt = (
                f"「{place}」のおすすめ観光スポットを{count}件提案してください。\n"
                f"重視したいジャンル: {interest_text}\n"
                "各スポットについて、カテゴリ・説明・おすすめする理由・訪れるのに"
                "おすすめの季節や時間帯を含めてください。"
            )
            result = call_ai(prompt, TouristSpotList, lambda: demo_data.demo_spots(place, count))
            if result:
                st.session_state["spots_result"] = (place, result)

    if "spots_result" in st.session_state:
        place, result = st.session_state["spots_result"]
        idx = 0
        for pattern in bento_rows(len(result.spots)):
            cols = st.columns(pattern, gap="medium")
            for col, width in zip(cols, pattern):
                spot = result.spots[idx]
                icon = "✨" if width == 2 else "📍"
                with col, st.expander(f"{icon} {spot.name}", expanded=True):
                    st.markdown(
                        f'<span class="bento-badge">{spot.category}</span>',
                        unsafe_allow_html=True,
                    )
                    st.write(spot.description)
                    st.markdown(f"**おすすめの理由:** {spot.why_recommended}")
                    st.markdown(f"**おすすめの時期・時間帯:** {spot.best_time}")
                    favorite_button(
                        "観光スポット",
                        f"{place} / {spot.name}",
                        spot.model_dump(),
                        f"fav_spot_{idx}",
                    )
                idx += 1

# ---------------------------------------------------------------------------
# Tab 2: Mood-based destination matcher
# ---------------------------------------------------------------------------
with tabs[1]:
    st.subheader("行きたい雰囲気やイメージから、旅行先を提案します")
    with st.form("mood_form"):
        mood = st.text_area(
            "どんな旅行がしたいか自由に書いてください",
            placeholder="例: 海が見える静かな場所でのんびりしたい、人混みは避けたい",
            height=100,
        )
        region = st.selectbox("地域の希望(任意)", REGIONS)
        budget = st.selectbox("予算感(任意)", ["指定なし", "リーズナブル", "standard", "贅沢"])
        n_suggestions = st.slider("提案数", 2, 6, 3)
        submitted2 = st.form_submit_button("旅行先を提案してもらう", type="primary")

    if submitted2:
        if not mood.strip():
            st.warning("どんな旅行がしたいか入力してください。")
        else:
            prompt = (
                f"以下の希望に合う旅行先を{n_suggestions}件提案してください。\n"
                f"希望・雰囲気: {mood}\n"
                f"地域の希望: {region}\n"
                f"予算感: {budget}\n"
                "各提案について、地域、概要、見どころ、簡単な旅行プラン例、"
                "なぜこの希望にマッチするかの理由を含めてください。"
            )
            result = call_ai(
                prompt,
                DestinationSuggestionList,
                lambda: demo_data.demo_destinations(mood, region, n_suggestions),
            )
            if result:
                st.session_state["dest_result"] = result

    if "dest_result" in st.session_state:
        result = st.session_state["dest_result"]
        idx = 0
        for pattern in bento_rows(len(result.suggestions)):
            cols = st.columns(pattern, gap="medium")
            for col, width in zip(cols, pattern):
                dest = result.suggestions[idx]
                icon = "✨" if width == 2 else "🌍"
                with col, st.expander(f"{icon} {dest.destination}", expanded=True):
                    st.markdown(
                        f'<span class="bento-badge">{dest.region}</span>',
                        unsafe_allow_html=True,
                    )
                    st.write(dest.summary)
                    st.markdown("**見どころ:**")
                    for h in dest.highlights:
                        st.markdown(f"- {h}")
                    st.markdown(f"**プラン例:** {dest.suggested_plan}")
                    st.markdown(f"**マッチする理由:** {dest.match_reason}")
                    favorite_button(
                        "旅行先", dest.destination, dest.model_dump(), f"fav_dest_{idx}"
                    )
                idx += 1

# ---------------------------------------------------------------------------
# Tab 3: Mountain finder
# ---------------------------------------------------------------------------
with tabs[2]:
    st.subheader("標高・地域・難易度から、条件に合う山を探します")
    with st.form("mountain_form"):
        elevation = st.slider("標高の範囲(m)", 0, 4000, (500, 2000), step=100)
        m_region = st.selectbox("地域(任意)", REGIONS, key="mountain_region")
        difficulty = st.multiselect("難易度(任意・複数選択可)", DIFFICULTIES)
        extra = st.text_input(
            "その他の希望条件(任意)", placeholder="例: 紅葉が綺麗、日帰り可能、初心者向け"
        )
        n_mountains = st.slider("提案数", 2, 8, 4)
        submitted3 = st.form_submit_button("山を探す", type="primary")

    if submitted3:
        diff_text = "、".join(difficulty) if difficulty else "指定なし"
        prompt = (
            f"以下の条件に合う山を{n_mountains}件提案してください。\n"
            f"標高の範囲: {elevation[0]}m 〜 {elevation[1]}m\n"
            f"地域: {m_region}\n"
            f"難易度: {diff_text}\n"
            f"その他の希望: {extra or 'なし'}\n"
            "各山について、標高、地域、難易度、標準コースタイム、見どころ、"
            "登山口へのアクセス、装備や注意点を含めてください。"
        )
        result = call_ai(
            prompt,
            MountainSuggestionList,
            lambda: demo_data.demo_mountains(elevation, m_region, difficulty, n_mountains),
        )
        if result:
            st.session_state["mountain_result"] = result

    if "mountain_result" in st.session_state:
        result = st.session_state["mountain_result"]
        idx = 0
        for pattern in bento_rows(len(result.mountains)):
            cols = st.columns(pattern, gap="medium")
            for col, width in zip(cols, pattern):
                mtn = result.mountains[idx]
                icon = "✨" if width == 2 else "⛰️"
                with col, st.expander(f"{icon} {mtn.name}　{mtn.elevation_m}m", expanded=True):
                    st.markdown(
                        f'<span class="bento-badge diff-{mtn.difficulty}">{mtn.difficulty}</span>',
                        unsafe_allow_html=True,
                    )
                    st.markdown(f"**地域:** {mtn.region}　|　**標準コースタイム:** {mtn.standard_duration}")
                    st.markdown(f"**見どころ:** {mtn.highlights}")
                    st.markdown(f"**アクセス:** {mtn.access}")
                    st.markdown(f"**注意点:** {mtn.notes}")
                    favorite_button("山", mtn.name, mtn.model_dump(), f"fav_mtn_{idx}")
                idx += 1

# ---------------------------------------------------------------------------
# Tab 4: Trip itinerary generator
# ---------------------------------------------------------------------------
with tabs[3]:
    st.subheader("目的地と条件を入力すると、日程プランを自動生成します")
    with st.form("plan_form"):
        destination = st.text_input("目的地", placeholder="例: 沖縄, 京都, パリ")
        days = st.number_input("日数", min_value=1, max_value=14, value=2)
        companion = st.selectbox(
            "同行者", ["一人旅", "カップル・夫婦", "家族(子供連れ)", "友人グループ"]
        )
        plan_interests = st.multiselect("興味のあるジャンル(任意)", INTERESTS, key="plan_interests")
        plan_budget = st.selectbox(
            "予算感", ["指定なし", "リーズナブル", "standard", "贅沢"], key="plan_budget"
        )
        submitted4 = st.form_submit_button("旅行プランを作成する", type="primary")

    if submitted4:
        if not destination.strip():
            st.warning("目的地を入力してください。")
        else:
            interest_text = "、".join(plan_interests) if plan_interests else "指定なし"
            prompt = (
                f"「{destination}」への{days}日間の旅行プランを作成してください。\n"
                f"同行者: {companion}\n"
                f"興味のあるジャンル: {interest_text}\n"
                f"予算感: {plan_budget}\n"
                "日ごとに午前・午後・夜のプランと補足メモを含め、"
                "全体の概要・おおよその予算目安・旅のコツも含めてください。"
            )
            result = call_ai(
                prompt,
                TripPlan,
                lambda: demo_data.demo_trip_plan(destination, days, companion),
            )
            if result:
                st.session_state["trip_plan_result"] = (destination, result)

    if "trip_plan_result" in st.session_state:
        destination, plan = st.session_state["trip_plan_result"]
        st.markdown(f"### {plan.title}")
        st.write(plan.overview)
        for d in plan.days:
            with st.expander(f"Day {d.day}: {d.theme}", expanded=d.day == 1):
                st.markdown(f"**午前:** {d.morning}")
                st.markdown(f"**午後:** {d.afternoon}")
                st.markdown(f"**夜:** {d.evening}")
                if d.notes:
                    st.caption(d.notes)
        st.markdown(f"**予算目安:** {plan.budget_estimate}")
        st.markdown("**旅のコツ:**")
        for tip in plan.tips:
            st.markdown(f"- {tip}")
        favorite_button("旅行プラン", f"{destination} / {plan.title}", plan.model_dump(), "fav_plan")

# ---------------------------------------------------------------------------
# Tab 5: Packing list generator
# ---------------------------------------------------------------------------
with tabs[4]:
    st.subheader("旅行・登山の持ち物リストを自動生成します")
    with st.form("packing_form"):
        trip_type = st.radio("種類", ["観光旅行", "登山"], horizontal=True)
        season = st.selectbox("季節", ["春", "夏", "秋", "冬"])
        pack_days = st.number_input("日数", min_value=1, max_value=14, value=2, key="pack_days")
        pack_extra = st.text_input(
            "その他の条件(任意)", placeholder="例: 雪山, 海外, 子供連れ, キャンプ泊"
        )
        submitted5 = st.form_submit_button("持ち物リストを作成する", type="primary")

    if submitted5:
        prompt = (
            f"{trip_type}({season}・{pack_days}日間)の持ち物リストを作成してください。\n"
            f"その他の条件: {pack_extra or 'なし'}\n"
            "カテゴリごとに項目を分けて、リストの最後に注意点や"
            "アドバイスも添えてください。"
        )
        result = call_ai(
            prompt,
            PackingListResponse,
            lambda: demo_data.demo_packing(trip_type, season, pack_days),
        )
        if result:
            st.session_state["packing_result"] = (trip_type, season, result)

    if "packing_result" in st.session_state:
        trip_type, season, packing = st.session_state["packing_result"]
        cols = st.columns(2)
        for i, cat in enumerate(packing.categories):
            with cols[i % 2]:
                st.markdown(f"**{cat.category}**")
                for item in cat.items:
                    st.checkbox(item, key=f"pack_{i}_{item}")
        st.info(packing.advice)
        favorite_button(
            "持ち物リスト", f"{trip_type}({season})", packing.model_dump(), "fav_packing"
        )

# ---------------------------------------------------------------------------
# Tab 6: Favorites
# ---------------------------------------------------------------------------
with tabs[5]:
    st.subheader("保存したお気に入り")
    favorites = storage.load_favorites()
    if not favorites:
        st.info("まだお気に入りはありません。各タブの結果から追加できます。")
    else:
        for i, fav in enumerate(reversed(favorites)):
            real_index = len(favorites) - 1 - i
            with st.expander(f"[{fav['kind']}] {fav['title']}　({fav['saved_at']})"):
                st.json(fav["detail"])
                if st.button("🗑️ 削除", key=f"del_{real_index}"):
                    storage.remove_favorite(real_index)
                    st.rerun()
