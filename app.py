import csv
import streamlit as st
import re
from pathlib import Path
from collections import Counter


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

@st.cache_data(ttl=600)
def carregar_dados(caminho):

    dados = []

    with open(caminho, "r", encoding="utf-8-sig") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            linha["taxa_desocupacao"] = float(linha["taxa_desocupacao"])
            dados.append(linha)

    return dados

dados = carregar_dados(ARQUIVO)

st.subheader("Filtros de Empregabilidade")
regioes = ["Todas"] + sorted(set(linha["regiao"] for linha in dados))
regiao_selecionada = st.selectbox("Selecione uma região:", regioes)

if regiao_selecionada == "Todas":
    dados_regiao = dados
else:
    dados_regiao = [
        linha for linha in dados
        if linha["regiao"] == regiao_selecionada
    ]

estados = ["Todos"] + sorted(
    set(linha["estado"] for linha in dados_regiao)
)

estado_selecionado = st.selectbox("Selecione um estado:", estados)

if estado_selecionado == "Todos":
    dados_filtrados = dados_regiao
else:
    dados_filtrados = [
        linha for linha in dados_regiao
        if linha["estado"] == estado_selecionado
    ]

st.subheader("Resultados da Consulta")
st.write("Quantidade de registros:", len(dados_filtrados))
st.dataframe(dados_filtrados, width="stretch")

st.subheader("Comparação de Estados")

if "ufs_comparacao" not in st.session_state:
    st.session_state.ufs_comparacao = []

opcoes_estados = {
    linha["estado"]: linha["uf"]
    for linha in dados_filtrados
}

if opcoes_estados:
    estado_comparacao = st.selectbox("Selecione um estado para adicionar à comparação:", list(opcoes_estados.keys()))

    if st.button("Adicionar à comparação"):
        uf = opcoes_estados[estado_comparacao]

        if uf not in st.session_state.ufs_comparacao:
            st.session_state.ufs_comparacao.append(uf)

if st.button("Limpar comparação"):
    st.session_state.ufs_comparacao = []

dados_comparacao = [
    linha for linha in dados
    if linha["uf"] in st.session_state.ufs_comparacao
]

if dados_comparacao:
    st.write("Estados selecionados para comparação:")
    st.dataframe(dados_comparacao, width="stretch")
    st.bar_chart(dados_comparacao, x="estado", y="taxa_desocupacao")

else:
    st.info(
        "Selecione um estado e clique em "
        "'Adicionar à comparação'."
    )

st.subheader("Taxa de Desocupação dos Jovens por Estado")
st.write(
    "Comparação da taxa de desocupação dos jovens de 18 a 24 anos "
    "entre os estados brasileiros, de acordo com os filtros selecionados."
)

if dados_filtrados:

    st.bar_chart(dados_filtrados, x="estado", y="taxa_desocupacao")

else:

    st.warning("Não há dados disponíveis para os filtros selecionados.")

st.subheader("Notícias sobre Empregabilidade Jovem")

ARQUIVO_NOTICIAS = (BASE / "data" / "processed" / "noticias_empregabilidade.csv")

noticias = []

if ARQUIVO_NOTICIAS.exists():

    with open(ARQUIVO_NOTICIAS, "r", encoding="utf-8-sig") as arquivo:

        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            noticias.append(linha)

    st.write("Quantidade de notícias coletadas:", len(noticias))
    st.dataframe(noticias, width="stretch")

    for noticia in noticias:

        st.markdown(f"**{noticia['titulo']}**")
        st.write("Data:", noticia["data"][:10])
        st.write("Fonte:", noticia["fonte"])
        st.markdown(f"[Ler notícia completa]({noticia['url']})")
        st.divider()

    st.subheader("Palavras mais frequentes nas notícias")
    texto = " ".join(noticia["titulo"] for noticia in noticias)
    texto = texto.lower()
    palavras = re.findall(r"[a-zà-ÿ]{4,}", texto)
    palavras_vazias = ["para", "como", "entre", "mais", "menos", "sobre", "pela", "pelos", "pelas", "com", "uma", "esse", "essa"]
    palavras_filtradas = [
        palavra for palavra in palavras
        if palavra not in palavras_vazias
    ]

    contagem = Counter(palavras_filtradas)
    mais_frequentes = contagem.most_common(10)
    frequencias = []

    for palavra, quantidade in mais_frequentes:
        frequencias.append({"palavra": palavra, "frequencia": quantidade})

    if frequencias:
        st.bar_chart(frequencias, x="palavra", y="frequencia")
        st.caption(
            "Frequência das palavras nos títulos das notícias "
            "coletadas da Agência Brasil."
        )

    else:
        st.info(
            "Não há palavras disponíveis para análise."
        )

else:
    st.warning("O arquivo de notícias não foi encontrado.")