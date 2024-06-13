import streamlit as st

# 페이지 컨텐츠를 함수로 정의
def render_sunpick_page():
    st.header("이곳은 선픽 페이지입니다.")
    st.write("선픽 페이지 내용을 여기에 작성하세요.")

def render_afterpick_page():
    st.header("이곳은 후픽 페이지입니다.")
    st.write("후픽 페이지 내용을 여기에 작성하세요.")

# 세션 스테이트 초기화
if 'page' not in st.session_state:
    st.session_state.page = '선픽'  # 기본값으로 "선픽" 페이지

# 사용자 정의 CSS 스타일 적용
st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-color: #2c2f38;
    }
    .sidebar .radio {
        color: white;
    }
    .css-1vgnldh, .css-1vgnldh:hover {
        color: white;
        background-color: #3E4249;
        border: 1px solid #3E4249;
        border-radius: 10px;
        padding: 10px 20px;
        margin: 5px 0;
        text-align: center;
        display: block;
    }
    .css-1vgnldh:hover {
        background-color: #545862;
    }
    .css-1vgnldh:focus {
        background-color: #4c4f58;
    }
    .css-1vgnldh:active {
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