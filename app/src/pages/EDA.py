import streamlit as st
from ui.eda import upload_sheet, view_sheet

st.set_page_config(
    page_title="Exploratory Data Analysis",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("Exploratory Data Analysis")


uploaded_file = upload_sheet()
view_sheet(uploaded_file)
