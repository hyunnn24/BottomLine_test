import streamlit as st

# 사용자 정의 CSS
st.markdown(
    """
    <style>
    /* 사이드바 배경색 및 내부 패딩 */
    .css-1d391kg {  /* 최신 Streamlit 버전에 따라 클래스 이름을 변경할 수 있습니다 */
        background-color: #333 !important;
        padding: 20px !important;
    }
    /* 사이드바 제목 스타일 설정 */
    .css-1aumxhk {
        color: #fff !important;
        text-align: center;
        font-size: 24px !important;
        margin-top: 0 !important;
        margin-bottom: 20px !important;
    }
    /* 라디오 버튼 컨테이너 스타일 설정 */
    .css-14xtw13 {
        display: flex !important;
        flex-direction: column !important;
    }
    /* 라디오 버튼 스타일 설정 */
    .css-qrbaxs {
        color: #fff !important;
        background-color: #444 !important;
        padding: 10px !important;
        margin: 5px 0 !important;
        border-radius: 5px !important;
        text-align: center !important;
        cursor: pointer !important;
        transition: background-color 0.3s ease !important;
    }
    /* 라디오 버튼 호버 상태 스타일 설정 */
    .css-qrbaxs:hover {
        background-color: #555 !important;
    }
    /* 라디오 버튼 포커스 상태 스타일 설정 */
    .css-qrbaxs:focus {
        background-color: #666 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 사이드바에 제목 추가
st.sidebar.title("OptimalBotAI")

# 사이드바에 라디오 버튼을 사용하여 페이지 선택
page = st.sidebar.radio("페이지 선택", ["선픽", "후픽"])

# 사용자가 선택한 페이지에 따라 다른 내용 표시
if page == "선픽":
    st.title("선픽 페이지")
    st.write("이곳은 선픽 페이지입니다.")
    # 선픽과 관련된 기능 추가
    option = st.selectbox('선픽할 항목을 선택하세요:', ['항목 1', '항목 2', '항목 3'])
    st.write(f'선택된 항목: {option}')
elif page == "후픽":
    st.title("후픽 페이지")
    st.write("이곳은 후픽 페이지입니다.")
    # 후픽과 관련된 기능 추가
    option = st.selectbox('후픽할 항목을 선택하세요:', ['항목 A', '항목 B', '항목 C'])
    st.write(f'선택된 항목: {option}')

# 공통 기능 추가 가능
st.write("공통 기능이나 추가 정보를 이곳에 넣을 수 있습니다.")
