import sqlite3

DB_NAME = "finance.db"

# -------------------------
# CONEXÃO
# -------------------------
def conectar():

    return sqlite3.connect(DB_NAME)

# -------------------------
# CRIAR TABELA
# -------------------------
def criar_tabela():

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT,
            valor REAL,
            descricao TEXT,
            categoria TEXT,
            data TEXT
        )
    """)

    conn.commit()
    conn.close()

# -------------------------
# INSERIR
# -------------------------
def inserir_transacao(transacao):

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO transacoes (
            tipo,
            valor,
            descricao,
            categoria,
            data
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        transacao["tipo"],
        transacao["valor"],
        transacao["descricao"],
        transacao["categoria"],
        transacao["data"]
    ))

    conn.commit()
    conn.close()

# -------------------------
# LISTAR
# -------------------------
def listar_transacoes():

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            tipo,
            valor,
            descricao,
            categoria,
            data
        FROM transacoes
    """)

    dados = cursor.fetchall()

    conn.close()

    transacoes = []

    for t in dados:

        transacoes.append({
            "id": t[0],
            "tipo": t[1],
            "valor": t[2],
            "descricao": t[3],
            "categoria": t[4],
            "data": t[5]
        })

    return transacoes