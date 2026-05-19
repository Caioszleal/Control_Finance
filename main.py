from finance import (
    nova_transacao,
    calcular_saldo,
    resumo,
    filtrar_categoria
)

from storage import carregar, salvar
from exporter import exportar_csv

transacoes = carregar()

while True:

    print("\n===== CONTROLE FINANCEIRO =====")
    print("1 - Adicionar receita")
    print("2 - Adicionar despesa")
    print("3 - Ver transações")
    print("4 - Ver saldo")
    print("5 - Ver resumo")
    print("6 - Filtrar categoria")
    print("7 - Exportar CSV")
    print("0 - Sair")

    opcao = input("Escolha: ")

    # RECEITA
    if opcao == "1":

        valor = float(input("Valor da receita: "))
        descricao = input("Descrição: ")
        categoria = input("Categoria: ")

        transacoes.append(
            nova_transacao(
                "receita",
                valor,
                descricao,
                categoria
            )
        )

        salvar(transacoes)

    # DESPESA
    elif opcao == "2":

        valor = float(input("Valor da despesa: "))
        descricao = input("Descrição: ")
        categoria = input("Categoria: ")

        transacoes.append(
            nova_transacao(
                "despesa",
                valor,
                descricao,
                categoria
            )
        )

        salvar(transacoes)

    # LISTAR
    elif opcao == "3":

        print("\n===== TRANSAÇÕES =====")

        for t in transacoes:

            simbolo = "+" if t["tipo"] == "receita" else "-"

            print(
                f"{t['data']} | "
                f"{simbolo} R${t['valor']} | "
                f"{t['categoria']} | "
                f"{t['descricao']}"
            )

    # SALDO
    elif opcao == "4":

        saldo = calcular_saldo(transacoes)

        print(f"\nSaldo atual: R${saldo}")

    # RESUMO
    elif opcao == "5":

        receitas, despesas, saldo = resumo(transacoes)

        print("\n===== RESUMO =====")
        print(f"Receitas: R${receitas}")
        print(f"Despesas: R${despesas}")
        print(f"Saldo: R${saldo}")

    # FILTRAR CATEGORIA
    elif opcao == "6":

        categoria = input("Categoria: ")
        filtradas = filtrar_categoria(
            transacoes, categoria
        )

        print(f"\n===== FILTRADAS =====")

        for t in filtradas:
            simbolo = "+" if t["tipo"] == "receita" else "-"
            print(
                f"{t['data']} | "
                f"{simbolo} R${t['valor']} | "
                f"{t['descricao']}"
            )

    # EXPORTAR CSV
    elif opcao == "7":

        exportar_csv(transacoes)

    elif opcao == "0":
        break

    else:
        print("Opção inválida")