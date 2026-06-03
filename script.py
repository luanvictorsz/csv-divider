import csv

#abaixo, coloque o diretorio e o nome do arquivo que deve ser dividido
arquivo_entrada = "C:\\teste\\arquivo.csv"

with open(arquivo_entrada, "r", encoding="utf-8", newline="") as f:
    total_linhas = sum(1 for _ in f) - 1

meio = total_linhas // 2

with open(arquivo_entrada, "r", encoding="utf-8", newline="") as entrada:
    leitor = csv.reader(
        entrada,
        delimiter=';',
        quotechar='"'
    )

    cabecalho = next(leitor)

    with open("arquivo_parte1.csv", "w", encoding="utf-8", newline="") as arq1, \
         open("arquivo_parte2.csv", "w", encoding="utf-8", newline="") as arq2:

        escritor1 = csv.writer(
            arq1,
            delimiter=';',
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL
        )

        escritor2 = csv.writer(
            arq2,
            delimiter=';',
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL
        )

        escritor1.writerow(cabecalho)
        escritor2.writerow(cabecalho)

        for i, linha in enumerate(leitor):
            if i < meio:
                escritor1.writerow(linha)
            else:
                escritor2.writerow(linha)

print(f"Total: {total_linhas}")
print(f"Parte 1: {meio}")
print(f"Parte 2: {total_linhas - meio}")
