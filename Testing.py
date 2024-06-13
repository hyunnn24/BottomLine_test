import streamlit as st

# 페이지 레이아웃 설정
col1, col2 = st.columns(2)

# 선픽 페이지
with col1:
    st.header("선픽 페이지")
    st.write("이곳은 선픽 페이지입니다.")
    # 선픽과 관련된 기능 추가
    option = st.selectbox('선픽할 항목을 선택하세요:', ['항목 1', '항목 2', '항목 3'], key='pre_pick')
    st.write(f'선택된 항목: {option}')

# 후픽 페이지
with col2:
    st.header("후픽 페이지")
    st.write("이곳은 후픽 페이지입니다.")
    # 후픽과 관련된 기능 추가
    option = st.selectbox('후픽할 항목을 선택하세요:', ['항목 A', '항목 B', '항목 C'], key='post_pick')
    st.write(f'선택된 항목: {option}')

# 공통 기능 추가 가능
st.write("공통 기능이나 추가 정보를 이곳에 넣을 수 있습니다.")