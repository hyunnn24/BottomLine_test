import streamlit as st

# 페이지 제목
st.sidebar.title("OptimalBotAI")

# 사이드바에서 페이지 옵션 선택
page = st.sidebar.radio("페이지를 선택하세요:", ["선픽", "후픽"])

# 선택한 페이지에 따른 내용 표시
if page == "선픽":
    st.header("이곳은 선픽 페이지입니다.")
    st.write("선픽 페이지 내용을 여기에 작성하세요.")
    # 여기에 선픽 페이지에 대한 추가 내용을 작성할 수 있습니다.
    
elif page == "후픽":
    st.header("이곳은 후픽 페이지입니다.")
    st.write("후픽 페이지 내용을 여기에 작성하세요.")
    # 여기에 후픽 페이지에 대한 추가 내용을 작성할 수 있습니다.