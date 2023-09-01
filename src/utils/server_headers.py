# import jwt
from streamlit.web.server.websocket_headers import _get_websocket_headers


def get_url() -> str or None:
    """Get the URL of the Streamlit app.
    Parameters
    ----------
    Returns:
    -------
        url: str
            The URL of the Streamlit app.
    """
    try:
        headers = _get_websocket_headers()
        return headers.get("Origin")
    except AttributeError:
        return None


# def get_amzn_oidc_data():
#     """Get the OIDC data from the Amazon headers.
#     Parameters
#     ----------
#     Returns:
#     -------
#         X-Amzn-Oidc-Data: dict
#             The OIDC data from the Amazon headers.
#     """
#     try:
#         headers = _get_websocket_headers()
#         options = {"verify_signature": False, "verify_aud": False}
#         data = jwt.decode(dict(headers)["X-Amzn-Oidc-Data"], options=options)
#         return data
#     except AttributeError:
#         return None
