from flask import Flask, request, jsonify

from finance import (
    nova_transacao,
    calcular_saldo
)

from storage import (
    carregar, 
    salvar
)

app = Flask(__name__)

transacoes = carregar()

#---------------------
# HOME
#---------------------
@app.route("/")
def home():

    return {
        "mensagem": "API Fincanceira Online 🚀"
    }

#---------------------
# LISTAR TRANSACOES
#---------------------
@app.route("/transacoes", methods=["GET"])
def listar_transacoes():

    return jsonify(transacoes)

#---------------------
# ADICIONAR TRANSACAO
#---------------------
@app.route("/transacoes", methods=["POST"])
def adicionar_transacao():

    dados = request.json

    nova = nova_transacao(
        dados["tipo"],
        dados["valor"],
        dados["descricao"]
        ,dados["categoria"]
    )

    transacoes.append(nova)

    salvar(transacoes)

    return jsonify({
        "mensagem": "Transação adicionada com sucesso!",
        "transacao": nova
    })

#---------------------
# SALDO
#---------------------
@app.route("/saldo", methods=["GET"])
def saldo():

    total = calcular_saldo(transacoes)

    return jsonify({
        "saldo": total
    })

#---------------------
# RODAR SERVIDOR
#---------------------
if __name__ == "__main__":

    app.run(debug=True)
    