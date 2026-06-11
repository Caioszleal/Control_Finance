# 💰 Finance API

Uma API REST para controle financeiro pessoal desenvolvida em Python utilizando Flask e SQLite.

O projeto permite cadastrar receitas e despesas, consultar saldo, atualizar transações, remover registros e validar dados de entrada.

## 🚀 Tecnologias Utilizadas

* Python 3.x
* Flask
* SQLite
* Pytest
* Pytest-Cov
* Ruff
* Black
* MyPy

---

## 📂 Estrutura do Projeto

```text
finance_api/
│
├── app.py
├── finance.py
├── database.py
├── validators.py
├── finance.db
├── requirements.txt
│
└── tests/
    ├── __init__.py
    └── test_api.py
```

---

## 🏗️ Arquitetura

O projeto segue uma arquitetura em camadas:

```text
Cliente HTTP
      │
      ▼
Flask API (app.py)
      │
      ▼
Business Layer (finance.py)
      │
      ▼
Data Layer (database.py)
      │
      ▼
SQLite Database
```

### Responsabilidades

| Arquivo       | Responsabilidade         |
| ------------- | ------------------------ |
| app.py        | Rotas e endpoints da API |
| finance.py    | Regras de negócio        |
| database.py   | Persistência SQLite      |
| validators.py | Validação de dados       |
| tests/        | Testes automatizados     |

---

## ⚙️ Instalação

Clone o repositório:

```bash
git clone https://github.com/Caioszleal/finance-api.git

cd finance-api
```

Crie um ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## ▶️ Executando o Projeto

```bash
python app.py
```

A API estará disponível em:

```text
http://127.0.0.1:5000
```

---

## 📌 Endpoints

### Home

```http
GET /
```

Resposta:

```json
{
  "mensagem": "API Financeira SQLite 🚀"
}
```

---

### Listar Transações

```http
GET /transacoes
```

---

### Buscar Transação por ID

```http
GET /transacoes/<id>
```

Exemplo:

```http
GET /transacoes/1
```

---

### Criar Transação

```http
POST /transacoes
```

Body:

```json
{
  "tipo": "receita",
  "valor": 5000,
  "descricao": "Salário",
  "categoria": "Trabalho"
}
```

---

### Atualizar Transação

```http
PUT /transacoes/<id>
```

Body:

```json
{
  "tipo": "receita",
  "valor": 6500,
  "descricao": "Salário Atualizado",
  "categoria": "Trabalho"
}
```

---

### Remover Transação

```http
DELETE /transacoes/<id>
```

---

### Consultar Saldo

```http
GET /saldo
```

Resposta:

```json
{
  "saldo": 4700.0
}
```

---

## ✅ Validações

A API valida:

* Tipo deve ser "receita" ou "despesa"
* Valor deve ser maior que zero
* Descrição obrigatória
* Categoria obrigatória

Exemplo de erro:

```json
{
  "erros": [
    "Tipo deve ser 'receita' ou 'despesa'",
    "Valor deve ser maior que zero"
  ]
}
```

---

## 🧪 Testes

Executar todos os testes:

```bash
pytest
```

Executar com detalhes:

```bash
pytest -v
```

---

## 📊 Cobertura de Testes

Gerar relatório de cobertura:

```bash
pytest --cov=.
```

Gerar relatório HTML:

```bash
pytest --cov=. --cov-report=html
```

Abrir:

```text
htmlcov/index.html
```

---

## 🔍 Qualidade de Código

### Ruff

```bash
ruff check .
```

### Black

```bash
black .
```

### MyPy

```bash
mypy .
```

---

## 🎯 Funcionalidades

* Cadastro de receitas
* Cadastro de despesas
* Consulta de saldo
* Atualização de transações
* Exclusão de transações
* Busca por ID
* Persistência SQLite
* Validação de dados
* Testes automatizados

---

## 🚀 Próximas Melhorias

* Autenticação JWT
* Swagger/OpenAPI
* SQLAlchemy ORM
* Dashboard com Streamlit
* Deploy em produção
* Docker
* CI/CD com GitHub Actions

---

## 👨‍💻 Autor

Projeto desenvolvido para estudos de Backend Python, APIs REST, SQLite e testes automatizados.
