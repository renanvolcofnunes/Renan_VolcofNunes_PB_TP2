# Organização do Projeto — CRISP-DM e TDSP

## 2. Método CRISP-DM 

### 2.1 Entendimento do Negócio

O projeto busca analisar os desafios relacionados à empregabilidade de jovens no Brasil, identificando diferenças entre regiões e compreendendo quais competências profissionais aparecem com maior frequência nas oportunidades de trabalho, são definidos nesta fase também as metas, os indicadores de sucesso, o ODS atendido e o público-alvo da aplicação.

### 2.2 Entendimento dos Dados

Buscaremos dados relacionados à empregabilidade jovem, características socioeconômicas e oportunidades de trabalho. As fontes serão avaliadas considerando sua disponibilidade, formato, cobertura geográfica, qualidade.

### 2.3 Preparação dos Dados

Será feita uma preparação como seleção das informações necessárias, conversão de tipos, tratamento de valores ausentes, padronização e entre outras preparações.

### 2.4 Modelagem

Os indicadores vão ser organizados e comparados entre estados e regiões, identificando localidades que apresentam maiores desafios relacionados à empregos.

### 2.5 Avaliação

Será verificado se o dashboard permite comparar as regiões brasileiras, identificar diferenças nos indicadores de empregabilidade e consultar as competências profissionais identificadas.

Caso os resultados não sejam suficientes  o projeto poderá retornar às etapas anteriores para ajustar os dados e etapas.

### 2.6 Implantação

O dashboard desenvolvido em Streamlit será executado e testado , nas etapas posteriores, poderá ser publicado.


## 3. Aplicação do TDSP ao projeto

### 3.1 Business Understanding

Nesta etapa são definidos o problema, os objetivos, as metas, os indicadores de sucesso, o ODS atendido e o público-alvo.

Para este projeto, o objetivo é compreender as diferenças regionais relacionadas à empregabilidade jovem e identificar as competências profissionais demandadas nas oportunidades analisadas.

### 3.2 Data Acquisition and Understanding

Serão coletada informações em fontes de dados onde poderão ser obtidos por arquivos, APIs e, nas etapas futuras do projeto, por Web Scraping. Após a coleta, será verificada a estrutura dos dados, os tipos das informações disponíveis.

### 3.3 Modeling

Inicialmente usaremos comparações entre indicadores de diferentes estados e regiões e a organização das competências identificadas nas oportunidades de trabalho.

### 3.4 Deployment

Python e Streamlit.

### 3.5 Customer Acceptance

A aplicação deverá ser avaliada considerando se as informações apresentadas atendem às necessidades definidas no início do projeto, será verificado se os usuários conseguem identificar regiões com maiores desafios relacionados à empregabilidade jovem e consultar as competências profissionais encontradas nas oportunidades analisadas.


## 4. Relação entre CRISP-DM e TDSP

As duas metodologias possuem objetivos semelhantes.

O **Entendimento do Negócio** do CRISP-DM corresponde ao **Business Understanding** do TDSP.

As fases de **Entendimento dos Dados e Preparação dos Dados** do CRISP-DM são reunidas no estágio de **Data Acquisition and Understanding** do TDSP.

A fase de **Modelagem* liga  correspondência direta com o estágio de **Modeling**.

Por fim, as fases de **Avaliação e Implantação** do CRISP-DM estão relacionadas aos estágios de **Deployment e Customer Acceptance** do TDSP.

Dessa forma, o CRISP-DM será utilizado como referência para compreender as etapas de um projeto de dados, enquanto o TDSP auxiliará na organização.