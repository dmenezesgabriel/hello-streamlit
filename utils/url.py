import urllib.parse as urlparse

from streamlit.runtime.scriptrunner import get_script_run_ctx


def get_query_params():
    ctx = get_script_run_ctx()
    if ctx is None:
        return {}
    return urlparse.parse_qs(ctx.query_string)
