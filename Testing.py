import streamlit as st

# 사용자 정의 CSS
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #333;
        padding: 20px;
    }
    .sidebar .sidebar-content h1 {
        color: #fff;
        text-align: center;
        font-size: 24px;
        margin-top: 0;
        margin-bottom: 20px;
    }
    .sidebar .sidebar-content .stRadio > label {
        display: none;
    }
    .sidebar .sidebar-content .stRadio > div {
        display: flex;
        flex-direction: column;
    }
    .sidebar .sidebar-content .stRadio div div {
        color: #fff;
        background-color: #444;
        padding: 10px;
        margin: 5px 0;
        border-radius: 5px;
        text-align: center;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .sidebar .sidebar-content .stRadio div div:hover {
        background-color: #555;
    }
    .sidebar .sidebar-content .stRadio div div:focus {
        background-color: #666;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 페이지 타이틀
st.sidebar.title("OptimalBotAI")

# 버튼을 사용하여 페이지 선택
page = st.sidebar.radio("페이지 선택", ["선픽", "후픽"])

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