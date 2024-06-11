import streamlit as st

# CSS를 사용하여 메인 페이지 스타일 지정
main_page_style = '''
<style>
/* 메인 페이지 배경 이미지 */
[data-testid="stAppViewContainer"] {
    background-image: url("https://cdn12.idcgames.com/storage/image/1100/lol-news/default.jpg");
    background-size: cover;
    background-position: center;
}

/* 메인 페이지 컨텐츠 스타일 */
[data-testid="stAppViewContainer"] .main {
    background-color: rgba(255, 255, 255, 0); /* 투명도 조절 */
    padding: 2rem;
    border-radius: 10px;
}

/* 타이틀 스타일 */
[data-testid="stAppViewContainer"] .main h1 {
    color: #ffffff; /* 타이틀 텍스트 색상 */
    text-align: center; /* 텍스트 가운데 정렬 */
}

/* 텍스트 스타일 */
.center-text {
    text-align: center; /* 텍스트 가운데 정렬 */
    color: #ffffff; /* 텍스트 색상 */
}

/* 버튼 스타일 */
.center-button {
    display: flex;
    justify-content: center; /* 버튼 가운데 정렬 */
    margin-top: 20px;
}
</style>
'''

# 현재 페이지 상태를 저장할 세션 상태 초기화
if 'page' not in st.session_state:
    st.session_state.page = 'main'

# 페이지 전환 함수
def switch_page(page_name):
    st.session_state.page = page_name

# 메인 페이지 함수
def main_page():
    # CSS 적용
    st.markdown(main_page_style, unsafe_allow_html=True)
    
    # 메인 페이지 내용
    st.title('Duo statics')
    st.markdown('<p class="center-text">이상적인 조합, 최상의 결과</p>', unsafe_allow_html=True)
    
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')

    # 버튼을 가운데로 정렬하기 위해 columns 사용
    col1, col2, col3 = st.columns([3, 1, 3])
    with col2:
        if st.button('Play'):
            switch_page('second_page')

# 두 번째 페이지 함수
def second_page():
    st.title('Second Page')
    st.write('이것은 두 번째 페이지입니다.')
    
    # 이전 페이지로 돌아가는 버튼
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button('이전 페이지로 돌아가기'):
            switch_page('main')
    
    # 다음 페이지로 이동하는 버튼
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button('세 번째 페이지로 이동'):
            switch_page('third_page')

# 세 번째 페이지 함수
def third_page():
    st.title('Third Page')
    st.write('이것은 세 번째 페이지입니다.')
    
    # 두 번째 페이지로 돌아가는 버튼
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button('두 번째 페이지로 돌아가기'):
            switch_page('second_page')

# 현재 페이지에 따라 해당 페이지 함수 호출
if st.session_state.page == 'main':
    main_page()
elif st.session_state.page == 'second_page':
    second_page()
elif st.session_state.page == 'third_page':
    third_page()
