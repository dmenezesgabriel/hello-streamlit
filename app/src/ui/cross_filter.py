import pandas as pd
import plotly.express as px
import streamlit as st
from plotly import graph_objects as go


def render_preview_ui(df: pd.DataFrame):
    with st.expander("Preview"):
        st.dataframe(df)


def build_bill_to_tip_figure(df: pd.DataFrame) -> go.Figure:
    fig = px.scatter(
        df,
        x="total_bill",
        y="tip",
        hover_data=["total_bill", "tip", "day"],
        height=800,
        title="Total Bill vs Tip",
    )
    return fig


def build_size_to_time_figure(df: pd.DataFrame) -> go.Figure:
    return px.density_heatmap(df, x="size", y="time", height=400)


def build_day_figure(df: pd.DataFrame) -> go.Figure:
    return px.histogram(df, x="day", height=400)


def render_plotly_ui(df: pd.DataFrame):
    bill_to_tip_figure = build_bill_to_tip_figure(df)
    size_to_time_figure = build_size_to_time_figure(df)
    day_figure = build_day_figure(df)

    c1, c2 = st.columns(2)

    with c1:
        st.plotly_chart(bill_to_tip_figure)
    with c2:
        st.plotly_chart(size_to_time_figure)
        st.plotly_chart(day_figure)
