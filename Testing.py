import streamlit as st

def page1():
    st.title("Page 1")
    st.write("Welcome to Page 1")
    st.write("This is a simple Streamlit app with two pages.")

def page2():
    st.title("Page 2")
    st.write("Welcome to Page 2")
    st.write("This is a simple Streamlit app with two pages.")

PAGES = {
    "Page 1": page1,
    "Page 2": page2
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]
page()
