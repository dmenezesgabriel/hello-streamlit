import plotly.express as px
import streamlit as st
from components.plotly_events import plotly_events


def main():
    st.title("Plotly Events")

    df = px.data.iris()
    fig = px.scatter(
        df, x="sepal_width", y="sepal_length", title="Sample Figure"
    )

    value = plotly_events(fig)
    st.write("Received", value)


main()
