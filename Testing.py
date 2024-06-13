import streamlit as st

# 사이드바에 선픽과 후픽 선택 상자 추가
st.sidebar.header("선픽")
pre_pick_option = st.sidebar.selectbox('선픽할 항목을 선택하세요:', ['항목 1', '항목 2', '항목 3'], key='pre_pick')
st.sidebar.write(f'선택된 선픽 항목: {pre_pick_option}')

st.sidebar.header("후픽")
post_pick_option = st.sidebar.selectbox('후픽할 항목을 선택하세요:', ['항목 A', '항목 B', '항목 C'], key='post_pick')
st.sidebar.write(f'선택된 후픽 항목: {post_pick_option}')

# 메인 페이지에 선택된 값 표시
st.title("선픽 & 후픽 페이지")

st.header("선픽")
st.write(f'선택된 선픽 항목: {pre_pick_option}')

st.header("후픽")
st.write(f'선택된 후픽 항목: {post_pick_option}')

# 공통 기능 추가 가능
st.write("공통 기능이나 추가 정보를 이곳에 넣을 수 있습니다.")