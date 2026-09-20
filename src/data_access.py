import csv
from pathlib import Path

import requests

URL_ESTADOS = "https://servicodados.ibge.gov.br/api/v1/localidades/estados?orderBy=nome"

URL_IBGE = (
    "https://apisidra.ibge.gov.br/values/"
    "t/4094/"
    "n3/all/"
    "v/4099/"
    "p/last%201/"
    "c58/100052"
)

resposta = requests.get(URL_IBGE, timeout=20)
print("Status:", resposta.status_code)
resposta.raise_for_status()

dados = resposta.json()

resposta_estados = requests.get(URL_ESTADOS, timeout=20)
resposta_estados.raise_for_status()

estados = resposta_estados.json()

por_id = {}

for estado in estados:
    por_id[int(estado["id"])] = {
        "uf": estado["sigla"],
        "estado": estado["nome"],
        "regiao": estado["regiao"]["nome"]
    }

linhas = []

for registro in dados[1:]:
    id_uf = int(registro["D1C"])

    linha = dict(por_id[id_uf])

    linha["faixa_etaria"] = registro["D4N"]
    linha["taxa_desocupacao"] = float(registro["V"])
    linha["trimestre"] = registro["D3N"]

    linhas.append(linha)

print(linhas[:3])

BASE = Path(__file__).resolve().parent.parent
ARQUIVO_SAMPLE = BASE / "data" / "sample" / "empregabilidade_jovem.csv"

campos = [
    "uf",
    "estado",
    "regiao",
    "faixa_etaria",
    "taxa_desocupacao",
    "trimestre"
]

with open(ARQUIVO_SAMPLE, "w", newline="", encoding="utf-8-sig") as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=campos)

    escritor.writeheader()
    escritor.writerows(linhas)

print("Arquivo salvo em:", ARQUIVO_SAMPLE)
