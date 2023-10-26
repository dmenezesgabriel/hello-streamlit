import os

import streamlit.components.v1 as components

_component_func = components.declare_component(
    name="st_gtag", path=f"{os.path.dirname(__file__)}/frontend"
)


def st_gtag(*args, **kwargs):
    # Command pattern
    # return (func, func, func, ...)
    component_value = _component_func(*args, **kwargs)
    return component_value
