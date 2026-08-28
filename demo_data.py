"""Sample data used when demo mode is on, so the app works without a Gemini API key."""

from schemas import (
    DestinationSuggestion,
    DestinationSuggestionList,
    ItineraryDay,
    MountainSuggestion,
    MountainSuggestionList,
    PackingCategory,
    PackingListResponse,
    TouristSpot,
    TouristSpotList,
    TripPlan,
)

SPOT_TEMPLATES = [
    {
        "name": "{place}の旧市街エリア",
        "category": "歴史・文化",
        "description": "石畳の小道や伝統的な建物が並び、散策だけでも楽しめる歴史地区です。",
        "why_recommended": "街の成り立ちや文化を肌で感じられる、定番の観光エリアです。",
        "best_time": "午前中の涼しい時間帯",
    },
    {
        "name": "{place}展望タワー",
        "category": "絶景",
        "description": "{place}を一望できる展望スポット。晴れた日は遠くの山並みまで見渡せます。",
        "why_recommended": "街全体の地理感をつかめて写真映えもする、まず訪れたいスポットです。",
        "best_time": "夕方〜夜景の時間帯",
    },
    {
        "name": "{place}中央市場",
        "category": "グルメ",
        "description": "地元の食材や名物グルメが揃う市場。食べ歩きにもぴったりです。",
        "why_recommended": "その土地ならではの味を気軽に楽しめます。",
        "best_time": "午前中(品揃えが豊富な時間帯)",
    },
    {
        "name": "{place}近郊の自然公園",
        "category": "自然・絶景",
        "description": "緑豊かな公園で、季節ごとの花や紅葉が楽しめます。",
        "why_recommended": "観光の合間にのんびり過ごせる癒やしスポットです。",
        "best_time": "春(桜)・秋(紅葉)の季節",
    },
    {
        "name": "{place}伝統工芸体験館",
        "category": "体験",
        "description": "地元の伝統工芸を実際に体験できる施設。お土産作りにもおすすめです。",
        "why_recommended": "旅の思い出を形に残せる人気の体験スポットです。",
        "best_time": "時間に余裕のある午後",
    },
    {
        "name": "{place}ローカル温泉",
        "category": "温泉",
        "description": "地元の人にも愛される温泉施設で、旅の疲れを癒やせます。",
        "why_recommended": "観光で歩き疲れた体をリフレッシュできます。",
        "best_time": "観光後の夕方",
    },
    {
        "name": "{place}の夜景スポット",
        "category": "絶景",
        "description": "街の明かりを見下ろせる高台。デートや記念撮影にも人気です。",
        "why_recommended": "昼間とは違う街の表情を楽しめます。",
        "best_time": "日没後1時間ほど",
    },
    {
        "name": "{place}カフェ通り",
        "category": "グルメ",
        "description": "個性的なカフェや雑貨店が並ぶ通り。散策途中の休憩に最適です。",
        "why_recommended": "地元で人気のお店が集まっており、街歩きが一層楽しくなります。",
        "best_time": "午後のティータイム",
    },
    {
        "name": "{place}のパワースポット神社",
        "category": "歴史・文化",
        "description": "静かな境内が広がる、地元で古くから親しまれている神社です。",
        "why_recommended": "落ち着いた雰囲気の中で旅の安全を祈願できます。",
        "best_time": "朝の人が少ない時間帯",
    },
    {
        "name": "{place}直売所・道の駅",
        "category": "グルメ",
        "description": "地元産の野菜や特産品、お土産が揃うスポットです。",
        "why_recommended": "旅の最後にお土産をまとめて調達するのに便利です。",
        "best_time": "帰り道に立ち寄れる時間帯",
    },
]

DESTINATION_POOL = [
    {
        "destination": "京都",
        "region": "近畿",
        "summary": "寺社仏閣と町家の風情が残る、四季を通じて楽しめる古都です。",
        "highlights": ["清水寺周辺の散策", "嵐山の竹林", "町家カフェ巡り"],
        "suggested_plan": "1日目は東山エリアの寺社巡り、2日目は嵐山でのんびり過ごすプラン。",
    },
    {
        "destination": "金沢",
        "region": "中部",
        "summary": "伝統工芸と新鮮な海の幸が楽しめる、コンパクトに周遊できる街です。",
        "highlights": ["兼六園", "近江町市場での食べ歩き", "ひがし茶屋街"],
        "suggested_plan": "1日目は兼六園と茶屋街、2日目は市場グルメと美術館巡り。",
    },
    {
        "destination": "屋久島",
        "region": "九州・沖縄",
        "summary": "太古の自然が残る島で、静かに自然と向き合いたい人に向いています。",
        "highlights": ["白谷雲水峡のトレッキング", "縄文杉ツアー", "海沿いの温泉"],
        "suggested_plan": "1日目は白谷雲水峡を軽めに散策、2日目以降に本格的なトレッキング。",
    },
    {
        "destination": "直島",
        "region": "四国",
        "summary": "現代アートと瀬戸内の穏やかな景色が融合した、アート好きに人気の島です。",
        "highlights": ["地中美術館", "草間彌生の水玉かぼちゃ", "島内のカフェ巡り"],
        "suggested_plan": "1日かけて美術館を巡り、島の景色をのんびり楽しむプラン。",
    },
    {
        "destination": "上高地",
        "region": "中部",
        "summary": "穂高連峰を望む山岳リゾートで、静かな自然の中で過ごせます。",
        "highlights": ["河童橋からの眺め", "大正池の散策", "梓川沿いのハイキング"],
        "suggested_plan": "河童橋から大正池までの遊歩道を歩く、半日〜1日の自然散策プラン。",
    },
    {
        "destination": "富良野・美瑛",
        "region": "北海道",
        "summary": "花畑と丘の風景が広がる、のどかな景色に癒やされるエリアです。",
        "highlights": ["ラベンダー畑", "青い池", "パッチワークの丘ドライブ"],
        "suggested_plan": "レンタカーで丘を巡り、地元グルメを楽しむ1〜2日プラン。",
    },
    {
        "destination": "角館・田沢湖",
        "region": "東北",
        "summary": "武家屋敷の街並みと、静かな湖の景色を両方楽しめるエリアです。",
        "highlights": ["角館の武家屋敷通り", "田沢湖畔のドライブ", "地元の郷土料理"],
        "suggested_plan": "1日目は角館の街歩き、2日目は田沢湖でのんびりドライブ。",
    },
    {
        "destination": "鎌倉",
        "region": "関東",
        "summary": "海と寺社が近く、都心から日帰りでも楽しめる落ち着いた街です。",
        "highlights": ["長谷寺・大仏散策", "由比ヶ浜の海辺", "小町通りの食べ歩き"],
        "suggested_plan": "午前は寺社巡り、午後は海辺とカフェでのんびり過ごすプラン。",
    },
    {
        "destination": "石垣島",
        "region": "九州・沖縄",
        "summary": "透明度の高い海でのんびりリゾート気分を味わえるエリアです。",
        "highlights": ["川平湾の海めぐり", "離島めぐりツアー", "地元食堂でのグルメ"],
        "suggested_plan": "1日目は川平湾周辺、2日目は離島めぐりツアーに参加するプラン。",
    },
]

MOUNTAIN_POOL = [
    {
        "name": "高尾山",
        "elevation_m": 599,
        "region": "関東",
        "difficulty": "初級",
        "standard_duration": "往復3〜4時間",
        "highlights": "都心から好アクセスで、紅葉の名所としても人気の入門コース。",
        "access": "京王高尾山口駅から徒歩約5分で登山口。",
        "notes": "スニーカーでも登れる手軽さが魅力ですが、雨天時は滑りやすいので注意。",
    },
    {
        "name": "大山(神奈川)",
        "elevation_m": 1252,
        "region": "関東",
        "difficulty": "中級",
        "standard_duration": "往復5〜6時間",
        "highlights": "丹沢の名峰で、山頂からは相模湾や富士山を望める。",
        "access": "小田急線伊勢原駅からバスでケーブルカー駅へ。",
        "notes": "ケーブルカーを使えば体力に応じてコース調整が可能。",
    },
    {
        "name": "谷川岳",
        "elevation_m": 1977,
        "region": "関東",
        "difficulty": "中級",
        "standard_duration": "往復6〜7時間",
        "highlights": "ロープウェイでアクセスでき、稜線からの展望が見事な人気の山。",
        "access": "上越新幹線上毛高原駅からバス・ロープウェイ。",
        "notes": "天候の変化が激しいので防寒・雨具は必須。",
    },
    {
        "name": "木曽駒ヶ岳",
        "elevation_m": 2956,
        "region": "中部",
        "difficulty": "中級",
        "standard_duration": "ロープウェイ利用で往復3〜4時間",
        "highlights": "ロープウェイで一気に標高2600m付近まで上がれる、日本アルプス入門に人気の山。",
        "access": "駒ヶ根駅からバス・ロープウェイを乗り継ぎ。",
        "notes": "標高が高いため夏でも防寒着が必要。",
    },
    {
        "name": "富士山",
        "elevation_m": 3776,
        "region": "中部",
        "difficulty": "上級",
        "standard_duration": "山頂往復8〜10時間(1泊が一般的)",
        "highlights": "日本最高峰。ご来光を目指す登山者で夏山シーズンは賑わう。",
        "access": "各五合目まで登山バスでアクセス。",
        "notes": "高山病対策として無理のないペース配分が重要。",
    },
    {
        "name": "宮之浦岳(屋久島)",
        "elevation_m": 1936,
        "region": "九州・沖縄",
        "difficulty": "上級",
        "standard_duration": "日帰りは早朝出発で往復10時間前後",
        "highlights": "屋久島最高峰。原生林と苔むした森を抜けて山頂を目指す。",
        "access": "屋久島空港からバス・タクシーで登山口へ。",
        "notes": "天候が変わりやすい島の山のため、事前の情報収集が重要。",
    },
    {
        "name": "旭岳(大雪山)",
        "elevation_m": 2291,
        "region": "北海道",
        "difficulty": "中級",
        "standard_duration": "ロープウェイ利用で往復4〜5時間",
        "highlights": "北海道最高峰を含む山群。お花畑と雄大な景観が魅力。",
        "access": "旭川空港からバスでロープウェイ駅へ。",
        "notes": "夏でも防寒着が必須。天候急変に注意。",
    },
    {
        "name": "石鎚山",
        "elevation_m": 1982,
        "region": "四国",
        "difficulty": "中級",
        "standard_duration": "往復5〜6時間",
        "highlights": "西日本最高峰。鎖場のスリルと稜線からの絶景が楽しめる。",
        "access": "JR伊予西条駅からバス・ロープウェイ。",
        "notes": "鎖場が苦手な場合は迂回路もあり。",
    },
]

DAY_THEME_TEMPLATES = [
    {
        "theme": "定番観光を巡る日",
        "morning": "{destination}の代表的な観光スポットを訪れます。",
        "afternoon": "近隣の見どころを散策しながら移動します。",
        "evening": "地元の名物料理を味わう夕食タイムです。",
        "notes": "主要スポットは事前に開館時間を確認しておくと安心です。",
    },
    {
        "theme": "自然・アウトドアを楽しむ日",
        "morning": "{destination}近郊の自然スポットでゆっくり過ごします。",
        "afternoon": "軽いハイキングや散策で景色を楽しみます。",
        "evening": "温泉や宿でゆっくり体を休めます。",
        "notes": "歩きやすい靴と羽織れる上着があると快適です。",
    },
    {
        "theme": "グルメと街歩きの日",
        "morning": "地元市場や商店街で朝食・食べ歩きを楽しみます。",
        "afternoon": "路地裏のカフェや専門店を巡ります。",
        "evening": "評判の良いレストランで{destination}の食を堪能します。",
        "notes": "人気店は混雑することがあるので予約や時間に余裕を。",
    },
    {
        "theme": "お土産・カフェ巡りの日",
        "morning": "ゆっくりチェックアウトし、近場のカフェで朝食。",
        "afternoon": "お土産店や雑貨店を巡ります。",
        "evening": "帰路につく前に{destination}の夜景や街並みを楽しみます。",
        "notes": "荷物が増えるので、宅配便の利用も検討しましょう。",
    },
]

PACKING_TRAVEL = [
    {"category": "衣類", "items": ["着替え(日数分+1)", "羽織れる上着", "歩きやすい靴", "室内着"]},
    {"category": "貴重品・書類", "items": ["身分証明書", "現金・カード", "予約確認書", "モバイルバッテリー"]},
    {"category": "電子機器", "items": ["スマートフォン充電器", "カメラ", "変換プラグ(海外の場合)"]},
    {"category": "洗面用具・日用品", "items": ["歯ブラシセット", "常備薬", "マスク", "エコバッグ"]},
]

PACKING_MOUNTAIN = [
    {"category": "ウェア", "items": ["レインウェア(上下)", "速乾性インナー", "防寒着", "登山靴", "帽子・手袋"]},
    {"category": "装備", "items": ["ザック(レインカバー付き)", "トレッキングポール", "ヘッドライト", "地図・コンパス"]},
    {"category": "行動食・水分", "items": ["行動食(チョコレート・ナッツ等)", "水・スポーツドリンク", "非常食"]},
    {"category": "安全対策", "items": ["救急セット", "モバイルバッテリー", "熊鈴(必要な場合)", "保険証・登山届"]},
]


def _cycle(pool: list[dict], n: int) -> list[dict]:
    if not pool:
        return []
    reps = (n // len(pool)) + 1
    return (pool * reps)[:n]


def demo_spots(place: str, count: int) -> TouristSpotList:
    place = place.strip() or "この街"
    chosen = _cycle(SPOT_TEMPLATES, count)
    spots = [
        TouristSpot(
            name=t["name"].format(place=place),
            category=t["category"],
            description=t["description"].format(place=place),
            why_recommended=t["why_recommended"],
            best_time=t["best_time"],
        )
        for t in chosen
    ]
    return TouristSpotList(spots=spots)


def demo_destinations(mood: str, region: str, n: int) -> DestinationSuggestionList:
    pool = DESTINATION_POOL
    if region and region != "指定なし":
        filtered = [d for d in pool if d["region"] == region] or pool
    else:
        filtered = pool
    chosen = _cycle(filtered, n)
    mood_text = mood.strip() or "のんびり過ごしたい"
    suggestions = [
        DestinationSuggestion(
            destination=d["destination"],
            region=d["region"],
            summary=d["summary"],
            highlights=d["highlights"],
            suggested_plan=d["suggested_plan"],
            match_reason=f"「{mood_text}」というご希望に近い、落ち着いた雰囲気のエリアです。",
        )
        for d in chosen
    ]
    return DestinationSuggestionList(suggestions=suggestions)


def demo_mountains(
    elevation_range: tuple[int, int], region: str, difficulties: list[str], n: int
) -> MountainSuggestionList:
    lo, hi = elevation_range
    pool = MOUNTAIN_POOL
    filtered = [m for m in pool if lo <= m["elevation_m"] <= hi] or pool
    if region and region != "指定なし":
        filtered = [m for m in filtered if m["region"] == region] or filtered
    if difficulties:
        filtered = [m for m in filtered if m["difficulty"] in difficulties] or filtered
    chosen = _cycle(filtered, n)
    mountains = [MountainSuggestion(**m) for m in chosen]
    return MountainSuggestionList(mountains=mountains)


def demo_trip_plan(destination: str, days: int, companion: str) -> TripPlan:
    destination = destination.strip() or "旅行先"
    day_templates = _cycle(DAY_THEME_TEMPLATES, days)
    itinerary = [
        ItineraryDay(
            day=i + 1,
            theme=t["theme"],
            morning=t["morning"].format(destination=destination),
            afternoon=t["afternoon"].format(destination=destination),
            evening=t["evening"].format(destination=destination),
            notes=t["notes"],
        )
        for i, t in enumerate(day_templates)
    ]
    return TripPlan(
        title=f"{destination} {days}日間のモデルプラン",
        overview=(
            f"{companion}向けに構成した、{destination}を満喫する{days}日間のサンプルプランです。"
        ),
        days=itinerary,
        budget_estimate="1人あたり目安 3〜6万円程度(交通費・宿泊費・食費込み、内容により変動)",
        tips=[
            "主要スポットは事前に営業時間・定休日を確認しておきましょう。",
            "移動の合間に休憩を挟み、無理のないペースで回るのがおすすめです。",
            "天候に応じて屋内スポットも組み合わせておくと安心です。",
        ],
    )


def demo_packing(trip_type: str, season: str, days: int) -> PackingListResponse:
    base = PACKING_MOUNTAIN if trip_type == "登山" else PACKING_TRAVEL
    categories = [PackingCategory(category=c["category"], items=list(c["items"])) for c in base]
    advice = (
        f"{season}の{trip_type}({days}日間)を想定したサンプルの持ち物リストです。"
        "気温や天候予報に合わせて、防寒・防水対策を調整してください。"
    )
    return PackingListResponse(categories=categories, advice=advice)
