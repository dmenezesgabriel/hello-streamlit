import random

import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Hello, World!",
    page_icon=":sunglasses:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Hello, World!")

st.header("This is a header", help="This is a tooltip", divider="rainbow")


st.markdown(
    """
    This is a :rainbow[Markdown]
    """
)

st.subheader("This is a subheader", help="This is a tooltip", divider="gray")

st.code(
    """
    import streamlit as st

    st.write("Hello, World!")
    """,
    language="python",
    line_numbers=True,
)

st.text("This is a text", help="This is a tooltip")

st.latex(
    r"""
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    """
)

st.caption("This is a caption", help="This is a tooltip")

st.divider()


df = pd.DataFrame(
    {
        "name": ["Roadmap", "Extras", "Issues"],
        "url": [
            "https://roadmap.streamlit.app",
            "https://extras.streamlit.app",
            "https://issues.streamlit.app",
        ],
        "stars": [random.randint(0, 1000) for _ in range(3)],
        "views_history": [
            [random.randint(0, 5000) for _ in range(30)] for _ in range(3)
        ],
        "isActive": [True, False, True],
    }
)


st.data_editor(
    df,
    column_config={
        "name": "App name",
        "stars": st.column_config.NumberColumn(
            "Github stars",
            help="This is a tooltip",
            format="%d ⭐",
        ),
        "url": st.column_config.LinkColumn("App URL"),
        "views_history": st.column_config.LineChartColumn(
            "Views history (past 30 days)", y_min=0, y_max=5000
        ),
    },
    hide_index=True,
    use_container_width=True,
    num_rows="fixed",
)
