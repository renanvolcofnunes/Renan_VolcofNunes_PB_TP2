import csv
from pathlib import Path

import streamlit as st


st.set_page_config(page_title="Empregabilidade Jovem no Brasil",
                   page_icon="📊", layout="wide")
st.title("Empregabilidade Jovem no Brasil")
st.subheader("Problema de Negócio")
st.write(
    """
    O projeto busca analisar os desafios relacionados à empregabilidade de jovens no Brasil,
    identificando diferenças entre regiões e compreendendo quais competências profissionais
    aparecem com maior frequência nas oportunidades de trabalho.
    """
)

st.subheader("Objetivos do Projeto")

st.markdown(
    """
    - Comparar indicadores de empregabilidade jovem entre estados e regiões brasileiras.
    - Identificar regiões com maiores desafios de inserção dos jovens no mercado de trabalho.
    - Identificar competências profissionais recorrentes nas oportunidades de trabalho.
    - Apresentar os resultados de forma organizada em um dashboard interativo.
    """
)

st.subheader("Links Úteis")
st.markdown(
    """
    - [IBGE / SIDRA](https://sidra.ibge.gov.br/)
    - [Ministério do Trabalho e Emprego](https://www.gov.br/trabalho-e-emprego/)
    - [Conecta Brasil](https://conectabrasil.org/home)
    - [Observatório do Terceiro Setor](https://observatorio3setor.org.br/)
    """
)
st.subheader("Amostra dos Dados")

BASE = Path(__file__).resolve().parent
ARQUIVO = BASE / "data" / "sample" / "empregabilidade_jovem.csv"

dados = []

with open(ARQUIVO, "r", encoding="utf-8-sig") as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        linha["taxa_desocupacao"] = float(linha["taxa_desocupacao"])
        dados.append(linha)

st.dataframe(dados, use_container_width=True)
