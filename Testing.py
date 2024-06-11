import streamlit as st

main_page_style = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://cloudfront-us-east-1.images.arcpublishing.com/infobae/YABJ7CAXOZDVHAXSDRSQQ7NJR4.jpg");
    background-size: cover;
    background-position: center;
}

/* 메인 페이지 컨텐츠 스타일 */
[data-testid="stAppViewContainer"] .main {
    background-color: rgba(255, 255, 255); /* 투명도 조절 */
    padding: 2rem;
    border-radius: 10px;
}

/* 타이틀 스타일 */
[data-testid="stAppViewContainer"] .main h1 {
    color: #ff6347; /* 타이틀 텍스트 색상 */
}
</style>
'''

# 현재 페이지 상태를 저장할 세션 상태 초기화
if 'page' not in st.session_state:
    st.session_state.page = 'main'

# 페이지 전환 함수
def switch_page(page_name):
    st.session_state.page = page_name

# 현재 페이지에 따라 다른 내용 표시
if st.session_state.page == 'main':
    # CSS 적용
    st.markdown(main_page_style, unsafe_allow_html=True)
    
    # 메인 페이지 내용
    st.title('Streamlit App with Styled Main Page')
    st.write('이 예제는 메인 페이지의 배경 이미지와 컨텐츠 스타일을 지정하는 방법을 보여줍니다.')
    
    # 다음 페이지로 이동하는 버튼
    if st.button('다음 페이지로 이동'):
        switch_page('next_page')

elif st.session_state.page == 'next_page':
    # 두 번째 페이지 내용
    st.title('Second Page')
    st.write('이것은 두 번째 페이지입니다.')
    
    # 메인 페이지로 돌아가는 버튼
    if st.button('메인 페이지로 돌아가기'):
        switch_page('main')
