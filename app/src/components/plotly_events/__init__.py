import os

import streamlit.components.v1 as components
from plotly.graph_objects import Figure

_RELEASE = False

if not _RELEASE:
    _component_func = components.declare_component(
        "plotly_events",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component(
        "plotly_events", path=build_dir
    )


def plotly_events(fig: Figure, key=None):
    """Create a new instance of "my_component".

    Parameters
    ----------
    fig: Figure
        A Plotly figure.
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    dict
        A dictionary of values the component sends back to the Streamlit

    """
    spec = fig.to_json()
    component_value = _component_func(spec=spec)
    return component_value
