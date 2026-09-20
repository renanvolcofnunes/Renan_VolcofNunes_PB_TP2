import csv
import time
import requests
from pathlib import Path
from urllib.robotparser import RobotFileParser
from bs4 import BeautifulSoup


BASE = Path(__file__).resolve().parent.parent
PASTA_RAW = BASE / "data" / "raw"
PASTA_PROCESSED = BASE / "data" / "processed"
ARQUIVO_CSV = PASTA_PROCESSED / "noticias_empregabilidade.csv"
ROBOTS_URL = "https://agenciabrasil.ebc.com.br/robots.txt"
AGENTE = "EmpregabilidadeJovemTP2/1.0 (projeto academico)"
URLS = ["https://agenciabrasil.ebc.com.br/economia/noticia/2026-08/desigualdades-marcam-formalizacao-do-trabalho-entre-jovens-brasileiros",
    "https://agenciabrasil.ebc.com.br/economia/noticia/2026-06/jovens-ocupados-sao-maioria-mas-62-milhoes-seguem-como-nem-nem"]

resposta_robots = requests.get(ROBOTS_URL, headers={"User-Agent": AGENTE}, timeout=20)
resposta_robots.raise_for_status()
robots = RobotFileParser()
robots.parse(resposta_robots.text.splitlines())
espera = robots.crawl_delay(AGENTE)

if espera is None:
    espera = 10

noticias = []

for numero, url in enumerate(URLS, start=1):

    permitido = robots.can_fetch(AGENTE, url)

    if not permitido:
        print("Coleta não permitida:", url)
        continue

    print("Coletando notícia:", numero)
  
    time.sleep(espera)
    resposta = requests.get(url, headers={"User-Agent": AGENTE}, timeout=30)

    print("Status:", resposta.status_code)

    resposta.raise_for_status()
    caminho_html = PASTA_RAW / f"noticia_{numero}.html"

    with open(caminho_html, "w", encoding="utf-8") as arquivo:
        arquivo.write(resposta.text)

    sopa = BeautifulSoup(resposta.text, "html.parser")
    titulo_tag = sopa.find("h1")

    if titulo_tag is None:
        print("Título não encontrado:", url)
        continue

    titulo = titulo_tag.get_text(" ", strip=True)
    data_tag = sopa.find("meta", property="article:published_time")

    if data_tag is not None:
        data = data_tag.get("content", "")
    else:
        data = ""

    noticia = {"titulo": titulo, "data": data, "url": url, "fonte": "Agência Brasil"}
    noticias.append(noticia)

if noticias:

    campos = ["titulo", "data", "url", "fonte"]

    with open(ARQUIVO_CSV, "w", newline="", encoding="utf-8-sig") as arquivo:

        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(noticias)

    print("Quantidade de notícias:", len(noticias))
    print("CSV salvo em:", ARQUIVO_CSV)

else:
    print("Nenhuma notícia foi coletada. CSV anterior preservado.")
    