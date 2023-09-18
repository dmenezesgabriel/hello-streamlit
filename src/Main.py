import streamlit as st

from ui.st_api_reference import (
    render_altair_advanced_ui,
    render_altair_basic_ui,
    render_bokeh_ui,
    render_chart_ui,
    render_dataframe_ui,
    render_input_widgets_ui,
    render_json_ui,
    render_matplotlib_ui,
    render_media_elements_ui,
    render_metric_ui,
    render_plotly_ui,
    render_text_ui,
    render_vega_lite_ui,
)

st.set_page_config(
    page_title="Hello, World!",
    page_icon=":sunglasses:",
    layout="wide",
    initial_sidebar_state="expanded",
)


def main():
    render_text_ui()
    render_dataframe_ui()
    render_json_ui()
    render_metric_ui()
    render_chart_ui()
    render_matplotlib_ui()
    render_altair_basic_ui()
    render_altair_advanced_ui()
    render_vega_lite_ui()
    render_plotly_ui()
    render_bokeh_ui()
    render_input_widgets_ui()
    render_media_elements_ui()


main()
