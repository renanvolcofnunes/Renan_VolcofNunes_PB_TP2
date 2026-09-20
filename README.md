# Empregabilidade Jovem no Brasil

Projeto desenvolvido para a disciplina Projeto de Bloco: Inteligência Artificial Aplicada.

A aplicação analisa indicadores relacionados à empregabilidade de jovens no Brasil e permite visualizar dados por estados e regiões brasileiras.

## Ambiente de Desenvolvimento

### Criar o ambiente virtual

No terminal, na pasta raiz do projeto, execute:

```powershell
python -m venv .venv

### Ativar o ambiente virtual

No Windows PowerShell:

    .\.venv\Scripts\Activate.ps1

### Instalar as dependências

    python -m pip install -r requirements.txt

### Executar a aplicação

    streamlit run app.py

A aplicação será aberta no navegador utilizando o endereço local informado pelo Streamlit.

## Funcionalidades do TP2

A aplicação de Empregabilidade Jovem no Brasil foi ampliada com as seguintes funcionalidades:

- Filtros interativos por região e estado brasileiro.
- Visualização das taxas de desocupação dos jovens por meio de tabelas e gráficos.
- Comparação de estados utilizando o estado de sessão do Streamlit.
- Coleta de notícias da Agência Brasil por meio de Web Scraping com BeautifulSoup.
- Visualização das notícias coletadas e análise da frequência das palavras presentes nos títulos.
- Upload de arquivos CSV com notícias complementares.
- Validação dos arquivos enviados e identificação da procedência dos dados.
- Download dos indicadores de empregabilidade conforme os filtros selecionados.
- Utilização de cache para otimizar a leitura dos dados.

## Coleta de Dados

### Indicadores de Empregabilidade

Os indicadores de empregabilidade jovem foram obtidos por meio da API do IBGE e armazenados no arquivo:

`data/sample/empregabilidade_jovem.csv`

O código de coleta dos indicadores está localizado em:

`src/data_access.py`

### Notícias sobre Empregabilidade

As notícias são coletadas separadamente da aplicação, utilizando Requests e BeautifulSoup.

Para executar a coleta:

    python src/coleta_web.py

As páginas HTML são armazenadas em `data/raw/`, enquanto as informações processadas são salvas em:

`data/processed/noticias_empregabilidade.csv`

O dashboard utiliza o arquivo CSV processado para apresentar as notícias e realizar a análise de frequência das palavras.


## Repositório e Aplicação Publicada

**GitHub:**

https://github.com/renanvolcofnunes/Renan_VolcofNunes_PB_TP2

**Streamlit Community Cloud:**

https://empregabilidade-jovem-renan-tp2-v2.streamlit.app/


## Organização do Projeto

- `app.py`: aplicação principal desenvolvida em Streamlit.
- `src/data_access.py`: coleta de dados do IBGE.
- `src/coleta_web.py`: coleta de notícias utilizando Web Scraping.
- `data/sample/`: dados de empregabilidade utilizados na aplicação.
- `data/raw/`: arquivos HTML originais das notícias coletadas.
- `data/processed/`: dados processados utilizados no dashboard.
- `docs/project_charter.md`: documentação do problema de negócio, objetivos, escopo e stakeholders.
- `docs/data_summary_report.md`: documentação das fontes de dados utilizadas.
- `docs/metodologia_projeto.md`: organização do projeto utilizando CRISP-DM e TDSP.
- `requirements.txt`: dependências necessárias para executar o projeto.