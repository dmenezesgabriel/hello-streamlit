import os

import streamlit.components.v1 as components
from plotly.graph_objects import Figure

_RELEASE = True

if not _RELEASE:
    _component_func = components.declare_component(
        "plotly_events",
        url="http://localhost:5173",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/dist")
    _component_func = components.declare_component(
        "plotly_events", path=build_dir
    )


def st_plotly_events(
    fig: Figure,
    click_event=True,
    select_event=True,
    hover_event=False,
    double_click_event=True,
    override_height=450,
    override_width="100%",
    key=None,
):
    """Create a new instance of "my_component".

    Parameters
    ----------
    fig: Figure
        A Plotly figure.
    click_event: bool
        Whether to send click events to the component.
    select_event: bool
        Whether to send select events to the component.
    hover_event: bool
        Whether to send hover events to the component.
    override_height: int
        The height of the component.
    override_width: int
        The width of the component.
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    dict
        A dictionary of values the component sends back to the Streamlit

    """
    component_value = _component_func(
        fig=fig.to_json(),
        click_event=click_event,
        select_event=select_event,
        hover_event=hover_event,
        double_click_event=double_click_event,
        override_height=override_height,
        override_width=override_width,
        key=key,
        default=[],
    )
    return component_value


if __name__ == "__main__":
    import plotly.express as px
    import streamlit as st

    st.set_page_config(
        page_title="Plotly Events",
        page_icon=":bar_chart:",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    def get_plotly_events(fig):
        return st_plotly_events(
            fig, click_event=True, select_event=True, key="selected_points"
        )

    def main():
        st.title("Plotly Events")

        df = px.data.iris()
        fig = px.scatter(
            df,
            x="sepal_width",
            y="sepal_length",
            title="Sample Figure",
        )
        fig["layout"]["uirevision"] = True

        value = get_plotly_events(fig)
        plot_value_holder = st.empty()
        plot_value_holder.write(value)

    main()
