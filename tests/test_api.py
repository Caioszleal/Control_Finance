import pytest
from app import app

@pytest.fixture
def client():

    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client

def test_home(client):

    response = client.get("/")

    assert response.status_code == 200
    dados = response.get_json()
    assert "mensagem" in dados

def test_criar_transacao(client):

    response = client.post(
        "/transacoes",
        json={
            "tipo": "receita",
            "valor": 1000,
            "descricao": "Teste",
            "categoria": "Estudo"
        }
    )
    assert response.status_code == 200
    dados = response.get_json()
    assert "mensagem" in dados

def test_listar_transacoes(client):

    response = client.get("/transacoes")

    assert response.status_code == 200
    dados = response.get_json()
    assert isinstance(dados, list)

def test_saldo(client):

    response = client.get("/saldo")

    assert response.status_code == 200
    dados = response.get_json()
    assert "saldo" in dados

def test_transacao_invalida(client):

    response = client.post(
        "/transacoes",
        json={
            "tipo": "Banana",
            "valor": -1000,
        }
    )
    assert response.status_code == 400
    dados = response.get_json()
    assert "erros" in dados

def test_buscar_inexistente(client):

    response = client.get(
        "/transacoes/9999"
    )

    assert response.status_code == 404
    dados = response.get_json()
    assert "erro" in dados