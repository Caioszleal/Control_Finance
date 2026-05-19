import json
import os

ARQUIVO = os.path.join(os.path.dirname(__file__), "dados.json")

def carregar():
    if os.path.exists(ARQUIVO):
        try:
            with open(ARQUIVO, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, ValueError):
            return []
    return []

def salvar(transacoes):
    with open(ARQUIVO, "w") as f:
        json.dump(transacoes, f, indent=2)