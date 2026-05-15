import json
import os

ARQUIVO = "dados.json"

def carregar():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return []

def salvar(transacoes):
    with open(ARQUIVO, "w") as f:
        json.dump(transacoes, f, indent=2)