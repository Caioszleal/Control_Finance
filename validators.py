def validar_transacao(transacao):
    
    erros = []

    if "tipo" not in transacao:
        erros.append("Campo 'tipo' é obrigatório.")

    elif transacao ["tipo"] not in ["receita", "despesa"]:
        erros.append(
            "Campo 'tipo' deve ser 'receita' ou 'despesa'."
        )

    if "valor" not in transacao:
        erros.append("Campo 'valor' é obrigatório.")

    elif transacao ["valor"] <= 0:
        erros.append("Campo 'valor' deve ser maior que zero.")

    if not transacao.get("descricao"):
        erros.append("Campo 'descricao' é obrigatório.")

    if not transacao.get("categoria"):
        erros.append("Campo 'categoria' é obrigatório.")

    return erros
