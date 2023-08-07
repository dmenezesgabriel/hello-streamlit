import pandas as pd
import requests
import streamlit as st

st.title("Dados Brutos")

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
