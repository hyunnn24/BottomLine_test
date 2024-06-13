import streamlit as st

# 페이지 제목
st.title("선픽/후픽 페이지 선택")

# 페이지 옵션
options = ["선픽", "후픽"]

# 선택상자 생성
choice = st.selectbox("페이지를 선택하세요:", options)

# 선택한 페이지에 따른 내용 표시
if choice == "선픽":
    st.header("이곳은 선픽 페이지입니다.")
    st.write("선픽 페이지 내용을 여기에 작성하세요.")
    # 여기에 선픽 페이지에 대한 추가 내용을 작성할 수 있습니다.
    
elif choice == "후픽":
    st.header("이곳은 후픽 페이지입니다.")
    st.write("후픽 페이지 내용을 여기에 작성하세요.")
    # 여기에 후픽 페이지에 대한 추가 내용을 작성할 수 있습니다.