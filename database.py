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

# -------------------------
# BUSCAR
def buscar_transacao_por_id(id_transacao):

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
        WHERE id = ?
    """, (id_transacao,))

    resultado = cursor.fetchone()
    conn.close()

    if resultado is None:
        return None

    return {
        "id": resultado[0],
        "tipo": resultado[1],
        "valor": resultado[2],
        "descricao": resultado[3],
        "categoria": resultado[4],
        "data": resultado[5]
    }

# -------------------------
# ATUALIZAR
# -------------------------
def atualizar_transacao(id_transacao, dados):

    transacao_atual = buscar_transacao_por_id(id_transacao)

    if not transacao_atual:
        return False

    tipo = dados.get("tipo", transacao_atual["tipo"])
    valor = dados.get("valor", transacao_atual["valor"])
    descricao = dados.get("descricao", transacao_atual["descricao"])
    categoria = dados.get("categoria", transacao_atual["categoria"])
    data = dados.get("data", transacao_atual["data"])

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE transacoes
        SET
            tipo = ?,
            valor = ?,
            descricao = ?,
            categoria = ?,
            data = ?
        WHERE id = ?
    """, (
        tipo,
        valor,
        descricao,
        categoria,
        data,
        id_transacao
    ))

    conn.commit()

    linhas_afetadas = cursor.rowcount

    conn.close()

    return linhas_afetadas > 0


# -------------------------
# DELETAR
# -------------------------
def deletar_transacao(id_transacao):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM transacoes
        WHERE id = ?
    """, (id_transacao,))

    conn.commit()

    linhas_afetadas = cursor.rowcount

    conn.close()

    return linhas_afetadas > 0