import streamlit as st

from utils.analytics import st_track

st.set_page_config(
    page_title="Analytics",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded",
)

with st_track():
    st.button("Click me!", key="button1")

st.write(st.session_state.st_analytics)
