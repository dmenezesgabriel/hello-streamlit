import time

import pandas as pd
import requests
import streamlit as st

st.set_page_config(
    page_title="Dados Brutos",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("Dados Brutos")


@st.cache_data
def convert_csv(df):
    return df.to_csv(index=False).encode("utf-8")


def success_message():
    success = st.success("Download concluído com sucesso!", icon="✅")
    time.sleep(5)
    success.empty()


url: str = "https://labdados.com/produtos"

response = requests.get(url)
data = pd.DataFrame.from_dict(response.json())
data["Data da Compra"] = pd.to_datetime(
    data["Data da Compra"], format="%d/%m/%Y"
)

with st.expander("Colunas"):
    columns = st.multiselect(
        "Selecione as colunas", list(data.columns), list(data.columns)
    )

st.sidebar.title("Filtros")
with st.sidebar.expander("Nome do Produto"):
    products = st.multiselect(
        "Selecionar produtos",
        list(data["Produto"].unique()),
        list(data["Produto"].unique()),
    )
with st.sidebar.expander("Preço do Produto"):
    price = st.slider(
        "Preço do Produto",
        float(data["Preço"].min()),
        float(data["Preço"].max()),
        (float(data["Preço"].min()), float(data["Preço"].max())),
    )
with st.sidebar.expander("Data da Compra"):
    purchase_date = st.date_input(
        "Data da Compra",
        (data["Data da Compra"].min(), data["Data da Compra"].max()),
    )


query = """
Produto in @products and \
@price[0] <= Preço <= @price[1] and \
@purchase_date[0] <= `Data da Compra` <= @purchase_date[1]
"""

filtered_data = data.query(query)
filtered_data = filtered_data[columns]

st.dataframe(filtered_data)

st.markdown(
    f"A tabela possui :blue[{filtered_data.shape[0]}] linhas e :blue[{filtered_data.shape[1]}] colunas"
)

st.markdown("Escolha o nome do arquivo")
col1, col2 = st.columns(2)
with col1:
    filename = st.text_input("", label_visibility="collapsed", value="dados")
    filename = filename + ".csv"
with col2:
    button = st.download_button(
        "Download",
        data=convert_csv(filtered_data),
        file_name=filename,
        mime="text/csv",
        on_click=success_message,
    )
