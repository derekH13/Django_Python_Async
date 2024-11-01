import csv
from sys import argv
import seaborn as sns
# Extraindo as colunas hora e taxa
horas = []
taxas = []
# abrindo o arquivo para leitura
with open(file='./taxa-cdi.csv', mode='r', encoding='utf8') as fp:
    # lendo a primeira linha que é o cabeçalho e passando para proxima
    linha = fp.readline()
    linha = fp.readline()
    while linha:
        # transforma em lista usando como base a virgula
        linha_separada = linha.split(sep=',')
        hora = linha_separada[1]
        horas.append(hora)
        taxa = float(linha_separada[2])
        taxas.append(taxa)
        linha = fp.readline()
        # Salvando no grafico
 # é importante que as duas lista tenha o mesmo numero de elementos
grafico = sns.lineplot(x=horas, y=taxas)
# o titulo ta sendo passado pelo argv**
grafico.get_figure().savefig(f"{argv[1]}.png")

# lembrando que ele pega os valores da tabela em taxa-cdi.csv e faz um grafico
# por eu não ter conseguido preecher a tabela o grafico ira ficar em branco
