# Data Summary Report

## 1. Visão Geral

Será utilizada uma fonte oficial de dados públicos para analisar indicadores de empregabilidade por região e Unidade da Federação. Outras fontes poderão ser incorporadas nas próximas etapas para complementar a análise com informações sobre oportunidades e competências profissionais.


## 2. Fontes de Dados

### Fonte 1 — IBGE / SIDRA / PNAD Contínua

**Fonte:** IBGE — Sistema IBGE de Recuperação Automática (SIDRA), utilizando dados da PNAD Contínua.

**Tipo de dado:** Semi-estruturado, em formato JSON, obtido por meio de API.

**Objetivo de uso:** Indicadores relacionados à ocupação, desocupação e participação dos jovens no mercado de trabalho para permitir comparações entre estados e regiões brasileiras.

### Fonte 2 — Ministério do Trabalho e Emprego / Guia Brasileiro de Ocupações

**Fonte:** Ministério do Trabalho e Emprego — Guia Brasileiro de Ocupações e Classificação Brasileira de Ocupações (CBO).

**Tipo de dado:** Estruturado e textual, disponibilizado em painéis e bases públicas.

**Objetivo de uso:** utilizar informações relacionadas às ocupações profissionais, atividades realizadas, conhecimentos e habilidades associadas às profissões para complementar a análise sobre competências profissionais relevantes para o mercado de trabalho.

## 3. Dados que serão utilizados

### Dados da Fonte 1 — IBGE / SIDRA / PNAD Contínua

- Unidade da Federação (UF).
- Região brasileira.
- Faixa etária dos jovens analisados.
- Quantidade de pessoas ocupadas.
- Quantidade de pessoas desocupadas.
- Taxa de desocupação.
- Nível de ocupação.

### Dados da Fonte 2 — Ministério do Trabalho e Emprego / Guia Brasileiro de Ocupações

- Nome da ocupação profissional.
- Código da ocupação na CBO.
- Descrição da ocupação.
- Atividades relacionadas à ocupação.
- Conhecimentos associados à profissão.
- Habilidades e competências relacionadas à ocupação.


## 4. Relação das Fontes com o Problema do Projeto

A Fonte 1, IBGE / SIDRA / PNAD Contínua, analisa indicadores de empregabilidade jovem entre estados e regiões brasileiras, identificando diferentes relacionadas à ocupação e desocupação dos jovens.

A Fonte 2, Ministério do Trabalho e Emprego / Guia Brasileiro de Ocupações, utiliza pra complementar a análise com informações sobre ocupações, atividades, conhecimentos e competências profissionais relacionadas ao mercado de trabalho.


## 5. Novas Fontes de Dados — TP2

### Fonte 3 — Agência Brasil / Empresa Brasil de Comunicação (EBC)

**Fonte:** Agência Brasil, portal de notícias da Empresa Brasil de Comunicação (EBC).

**Link:** https://agenciabrasil.ebc.com.br/

**Tipo de dado:** Dados semiestruturados, extraídos de páginas HTML por meio de Web Scraping com Requests e BeautifulSoup.

**Objetivo de uso:** Coletar notícias relacionadas à empregabilidade jovem, qualificação profissional e mercado de trabalho, complementando os indicadores apresentados no dashboard.

**Dados utilizados:**

- Título da notícia.
- Data de publicação.
- URL da notícia.
- Fonte da informação.

As informações são armazenadas em um arquivo CSV e utilizadas para apresentar notícias no dashboard e identificar as palavras mais frequentes nos títulos coletados.

### Fonte 4 — Arquivos CSV enviados pelos usuários

**Fonte:** Arquivos CSV enviados pelos usuários da aplicação por meio do Streamlit.

**Tipo de dado:** Dados estruturados em formato CSV.

**Objetivo de uso:** Permitir que os usuários adicionem notícias complementares relacionadas à empregabilidade jovem, ampliando as informações disponíveis para consulta e análise.

**Dados utilizados:**

- Título da notícia.
- Data de publicação.
- URL da notícia.
- Fonte da informação.
- Procedência dos dados.

Os arquivos enviados passam por uma validação antes de serem utilizados. As notícias adicionadas são armazenadas no estado de sessão do usuário e podem complementar a análise das notícias coletadas por Web Scraping.


## 6. Organização e Tratamento dos Dados

Os dados utilizados no projeto são organizados em diferentes diretórios, conforme sua finalidade.

### Dados do IBGE

Os indicadores de empregabilidade jovem foram obtidos por meio da API do IBGE e armazenados no arquivo `data/sample/empregabilidade_jovem.csv`.

O arquivo contém informações sobre as unidades da federação, regiões brasileiras, faixa etária, taxas de desocupação e período de referência.

Esses dados são utilizados nos filtros, tabelas, gráficos e na comparação entre estados brasileiros.

### Dados coletados por Web Scraping

A coleta das notícias é realizada separadamente da aplicação Streamlit, utilizando o arquivo `src/coleta_web.py`.

Antes da coleta, são verificadas as regras de acesso do site por meio do arquivo robots.txt.

As páginas HTML coletadas são armazenadas no diretório `data/raw/`, enquanto as informações extraídas e organizadas são salvas em `data/processed/noticias_empregabilidade.csv`.

O arquivo CSV processado é utilizado pelo dashboard para apresentar as notícias e realizar a contagem das palavras mais frequentes nos títulos.

### Dados enviados pelos usuários

A aplicação permite o envio de arquivos CSV contendo notícias complementares.

Antes de incorporar os dados, são verificadas as colunas obrigatórias, o conteúdo do arquivo e sua codificação.

As notícias enviadas são armazenadas no `st.session_state` e identificadas pela procedência "Upload".

Os dados coletados por Web Scraping e os enviados pelos usuários são reunidos na análise conjunta, evitando a duplicação de notícias com a mesma URL.

Os arquivos enviados não são armazenados permanentemente no projeto.


## 7. Limitações dos Dados

Os indicadores de empregabilidade apresentados no dashboard correspondem à faixa etária de 18 a 24 anos e ao período disponível na base utilizada.

As notícias coletadas da Agência Brasil complementam a análise dos indicadores, mas não representam todas as informações disponíveis sobre o mercado de trabalho brasileiro.

A análise de frequência das palavras considera os títulos das notícias coletadas e adicionadas pelos usuários, não sendo utilizada como medida direta da demanda por competências profissionais nas vagas de emprego.

Os dados enviados pelos usuários dependem da qualidade e da confiabilidade das fontes informadas nos arquivos CSV.

Nas próximas etapas do projeto, novas fontes poderão ser incorporadas para ampliar as análises relacionadas às oportunidades de trabalho e às competências profissionais demandadas.