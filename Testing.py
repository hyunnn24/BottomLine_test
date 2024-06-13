import streamlit as st

# 페이지 선택
page = st.sidebar.selectbox("페이지 선택", ["선픽"],["후픽"])

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