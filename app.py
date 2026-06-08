from flask import Flask, request, jsonify

from validators import validar_transacao

from finance import (
    nova_transacao,
    calcular_saldo
)

from database import (
    criar_tabela,
    inserir_transacao,
    listar_transacoes,
    atualizar_transacao,
    deletar_transacao,
    buscar_transacao_por_id
)

app = Flask(__name__)

# cria tabela ao iniciar
criar_tabela()

# -------------------------
# HOME
# -------------------------
@app.route("/")
def home():

    return {
        "mensagem": "API Financeira SQLite 🚀"
    }

# -------------------------
# LISTAR TRANSAÇÕES
# -------------------------
@app.route("/transacoes", methods=["GET"])
def transacoes():

    dados = listar_transacoes()

    return jsonify(dados)

# -------------------------
# ADICIONAR TRANSAÇÃO
# -------------------------
@app.route("/transacoes", methods=["POST"])
def adicionar():

    dados = request.json

    erros = validar_transacao(dados)

    if erros:
        return jsonify({"erros": erros}), 400

    nova = nova_transacao(
        dados["tipo"],
        dados["valor"],
        dados["descricao"],
        dados["categoria"]
    )

    inserir_transacao(nova)

    return jsonify({
        "mensagem": "Transação salva no banco!"
    })

# -------------------------
# ATUALIZAR TRANSAÇÃO
# -------------------------

@app.route("/transacoes/<int:id>", methods=["PUT", "PATCH"])
def atualizar(id):

    dados = request.get_json(silent=True)

    if dados is None:
        return jsonify({
            "mensagem": "Requisição inválida. Envie JSON com os campos da transação."
        }), 400

    erros = validar_transacao(dados)

    if erros:
        return jsonify({"erros": erros}), 400

    sucesso = atualizar_transacao(id, dados)

    if not sucesso:
        return jsonify({
            "mensagem": "Transação não encontrada!"
        }), 404
    
    return jsonify({
        "mensagem": "Transação atualizada com sucesso!"
    })

# -------------------------
# DELETAR TRANSAÇÃO
# -------------------------
@app.route("/transacoes/<int:id>", methods=["DELETE"])
def deletar(id):

    sucesso = deletar_transacao(id)

    if not sucesso:
        return jsonify({
            "mensagem": "Transação não encontrada!"
        }), 404

    return jsonify({
        "mensagem": "Transação removida com sucesso!"
    })

# -------------------------
# SALDO
# -------------------------
@app.route("/saldo", methods=["GET"])
def saldo():

    transacoes = listar_transacoes()

    total = calcular_saldo(transacoes)

    return jsonify({
        "saldo": total
    })

# -------------------------
# BUSCAR TRANSAÇÃO POR ID
# -------------------------
@app.route("/transacoes/<int:id>", methods=["GET"])
def buscar(id):

    transacao = buscar_transacao_por_id(id)

    if transacao is None:
        return jsonify({
            "erro": "Transação não encontrada!"
        }), 404

    return jsonify(transacao)

# -------------------------
# START
# -------------------------
if __name__ == "__main__":

    app.run(debug=True)