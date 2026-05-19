import csv

def exportar_csv(transacoes, arquivo="relatorio.csv"):
    with open(arquivo, mode='w', newline='', encoding='utf-8') as f:

        writer = csv.writer(f)

        writer.writerow([
            "Data",
            "Tipo", 
            "Valor",
            "Categoria",
            "Descrição"
        ])

        for t in transacoes:

            writer.writerow([
                t["data"],
                t["tipo"],
                t["valor"],
                t["categoria"],
                t["descricao"]
            ])

    print(f"\nArquivo '{arquivo}' exportado com sucesso!")
