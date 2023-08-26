import pandas as pd
import plotly.express as px
import streamlit as st
from plotly import graph_objects as go
from ui.cross_filter import render_plotly_ui, render_preview_ui

st.set_page_config(
    page_title="Cross Filter",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded",
)


@st.cache_data
def load_data() -> pd.DataFrame:
    return px.data.tips()


def main():
    st.title("Cross Filter")

    df = load_data()

    render_preview_ui(df)
    render_plotly_ui(df)


main()
