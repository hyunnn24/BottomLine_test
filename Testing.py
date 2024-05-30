import streamlit as st
from openai import OpenAI


def APIINPUT():
    st.header("API Key 를 입력하세요")
    API = st.text_input("API", type="password")
    if API:
        st.session_state.API = API

def page2():

def page3():

page = st.sidebar.selectbox("페이지 선택", ["API", "페이지2", "페이지3"])


if page == "API":
    APIINPUT()
elif page == "페이지2":
    page2()
elif page == "페이지3":
    page3()