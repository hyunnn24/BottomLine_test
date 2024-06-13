import streamlit as st
from PIL import Image, ImageDraw
import requests
from io import BytesIO

# 바텀 챔피언 목록
bottom_champions = {
    "Ashe": "https://ddragon.leagueoflegends.com/cdn/12.21.1/img/champion/Ashe.png",
    "Miss Fortune": "https://ddragon.leagueoflegends.com/cdn/12.21.1/img/champion/MissFortune.png",
    "Jhin": "https://ddragon.leagueoflegends.com/cdn/12.21.1/img/champion/Jhin.png",
    "Kaisa": "https://ddragon.leagueoflegends.com/cdn/12.21.1/img/champion/Kaisa.png",
    "Tristana": "https://ddragon.leagueoflegends.com/cdn/12.21.1/img/champion/Tristana.png",
    # 서포터 챔피언 추가
    "Leona": "https://ddragon.leagueoflegends.com/cdn/12.21.1/img/champion/Leona.png",
    "Nami": "https://ddragon.leagueoflegends.com/cdn/12.21.1/img/champion/Nami.png",
    "Lulu": "https://ddragon.leagueoflegends.com/cdn/12.21.1/img/champion/Lulu.png",
    "Thresh": "https://ddragon.leagueoflegends.com/cdn/12.21.1/img/champion/Thresh.png",
    "Blitzcrank": "https://ddragon.leagueoflegends.com/cdn/12.21.1/img/champion/Blitzcrank.png"
}

# 이미지를 원형으로 자르는 함수 정의
def crop_to_circle(image):
    np_image = np.array(image)
    h, w = image.size
    alpha = Image.new('L', image.size, 0)
    draw = ImageDraw.Draw(alpha)
    draw.pieslice([0, 0, h, w], 0, 360, fill=255)
    np_alpha = np.array(alpha)
    np_image = np.dstack((np_image, np_alpha))
    return Image.fromarray(np_image)

# 페이지 컨텐츠를 함수로 정의
def render_sunpick_page():
    st.header("이곳은 선픽 페이지입니다.")
    st.write("선픽 페이지 내용을 여기에 작성하세요.")

def render_afterpick_page():
    st.header("바텀 챔피언 목록")
    st.write("바텀 챔피언들의 얼굴 이미지입니다:")

    for champ, url in bottom_champions.items():
        response = requests.get(url)
        img = Image.open(BytesIO(response.content)).convert("RGBA")
        circ_img = crop_to_circle(img)
        st.image(circ_img, caption=champ)

# 세션 스테이트 초기화
if 'page' not in st.session_state:
    st.session_state.page = '선픽'  # 기본값으로 "선픽" 페이지

# 사용자 정의 CSS 스타일 적용
st.markdown("""
    <style>
    .css-1d391kg .stButton button {
        color: white;
        background-color: #3E4249;
        border: 1px solid #3E4249;
        border-radius: 10px;
        padding: 10px 20px;
        margin: 5px 0;
        text-align: center;
        display: block;
    }

    .css-1d391kg .stButton button:hover {
        background-color: #545862;
    }

    .css-1d391kg .stButton button:focus {
        background-color: #4c4f58;
    }

    .css-1d391kg .stButton button:active {
        background-color: #2a2d32;
    }
    </style>
    """, unsafe_allow_html=True)

# 페이지 제목
st.sidebar.title("OptimalBotAI")

# 사이드바에서 페이지 옵션 선택
if st.sidebar.button("선픽"):
    st.session_state.page = '선픽'
if st.sidebar.button("후픽"):
    st.session_state.page = '후픽'

# 현재 선택된 페이지에 따른 내용 표시
if st.session_state.page == '선픽':
    render_sunpick_page()
elif st.session_state.page == '후픽':
    render_afterpick_page()