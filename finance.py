from datetime import datetime

def nova_transacao(tipo, valor, descricao, categoria):

    return {
        "tipo": tipo,
        "valor": valor,
        "descricao": descricao,
        "categoria": categoria,
        "data": datetime.now().strftime("%d/%m/%Y")
    }

def calcular_saldo(transacoes):

    saldo = 0

    for t in transacoes:

        if t["tipo"] == "receita":
            saldo += t["valor"]
        else:
            saldo -= t["valor"]

    return saldo