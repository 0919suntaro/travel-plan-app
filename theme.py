import streamlit as st

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=M+PLUS+Rounded+1c:wght@400;500;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'M PLUS Rounded 1c', sans-serif;
}

.stApp {
    background-color: #FBF8F1;
    background-image:
        radial-gradient(circle at 8% 8%, rgba(58, 99, 81, 0.05) 0, transparent 40%),
        radial-gradient(circle at 95% 15%, rgba(201, 124, 93, 0.06) 0, transparent 35%);
}

section[data-testid="stSidebar"] {
    background-color: #EFE7D6;
    border-right: 1px solid #D9CFB8;
}

h1, h2, h3 {
    color: #2E4A3D !important;
}

.app-hero {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    margin-bottom: 0.2rem;
}

.app-divider {
    border: none;
    height: 3px;
    margin: 0.4rem 0 1.4rem 0;
    background: repeating-linear-gradient(
        90deg,
        #3A6351 0, #3A6351 10px,
        #C97C5D 10px, #C97C5D 16px,
        transparent 16px, transparent 22px
    );
    border-radius: 999px;
    opacity: 0.55;
}

/* Buttons */
.stButton > button,
.stFormSubmitButton > button {
    background-color: #3A6351;
    color: #FBF8F1;
    border: none;
    border-radius: 999px;
    padding: 0.5rem 1.4rem;
    font-weight: 600;
    transition: background-color 0.2s ease, transform 0.1s ease;
}
.stButton > button:hover,
.stFormSubmitButton > button:hover {
    background-color: #2E4A3D;
    color: #FBF8F1;
    transform: translateY(-1px);
}

/* Expander cards (spot / mountain / plan results) */
div[data-testid="stExpander"] {
    background-color: #FFFFFF;
    border: 1px solid #E4DCC8 !important;
    border-left: 5px solid #C97C5D !important;
    border-radius: 16px !important;
    box-shadow: 0 2px 8px rgba(46, 74, 61, 0.06);
    margin-bottom: 0.7rem;
    overflow: hidden;
}
div[data-testid="stExpander"] summary {
    font-weight: 600;
    color: #2E4A3D;
}

/* Tabs */
button[data-baseweb="tab"] {
    border-radius: 999px 999px 0 0;
    font-weight: 600;
}
div[data-baseweb="tab-highlight"] {
    background-color: #C97C5D;
}

/* Bento grid result cards */
div[data-testid="stHorizontalBlock"] {
    align-items: stretch;
}
.bento-badge {
    display: inline-block;
    background-color: #EFE7D6;
    color: #2E4A3D;
    padding: 2px 12px;
    border-radius: 999px;
    font-size: 0.78rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
}
.bento-badge.diff-初級 { background-color: #DCEAD9; color: #2E6B3E; }
.bento-badge.diff-中級 { background-color: #F5E3C6; color: #8A5A17; }
.bento-badge.diff-上級 { background-color: #F3D6CE; color: #9C3B24; }

/* Metric (favorites count) */
div[data-testid="stMetricValue"] {
    color: #3A6351;
}

/* Inputs */
div[data-baseweb="input"], div[data-baseweb="textarea"], div[data-baseweb="select"] {
    border-radius: 12px !important;
}
</style>
"""

HERO_HTML = """
<div class="app-hero">
    <span style="font-size:2.1rem;">🌲</span>
    <span style="font-size:2rem; font-weight:700; color:#2E4A3D;">
        旅行・登山 おすすめナビ
    </span>
</div>
<hr class="app-divider" />
"""


def inject_theme() -> None:
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


def render_hero() -> None:
    st.markdown(HERO_HTML, unsafe_allow_html=True)
