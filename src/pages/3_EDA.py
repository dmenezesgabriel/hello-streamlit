import streamlit as st
from ui.eda import render_preview_ui, upload_sheet

st.set_page_config(
    page_title="Exploratory Data Analysis",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded",
)


import pandas as pd
import streamlit as st


@st.cache_data
def load_data(file: str, **kwargs) -> pd.DataFrame:
    data = pd.read_csv(file, **kwargs)
    return data


def main():
    st.title("Exploratory Data Analysis")
    uploaded_file = upload_sheet()
    df = load_data(uploaded_file)
    render_preview_ui(df)


main()
