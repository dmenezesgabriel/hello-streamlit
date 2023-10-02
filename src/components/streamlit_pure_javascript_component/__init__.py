import os

import streamlit.components.v1 as components

st_pure_js_input = components.declare_component(
    name="example", path=f"{os.path.dirname(__file__)}/frontend"
)
