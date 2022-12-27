#-----------------------------------------------------
# txt 4 - O nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.
#-----------------------------------------
def contaRep(lista):
    """Funcao recebe uma lista e retorna outra lista com a contagem de repeticoes de cada elemento no modelo (count elemento)"""
    lista.sort()
    contagem = []
    rep = 0
    for element in range(0, len(lista)-1):
        if(str(lista[element]) == str(lista[element+1])):
            rep+=1
            if(element == len(lista)-2):
                contagem.append(str(rep+1) +' '+ lista[element])
                rep = 0
        else:
            contagem.append(str(rep+1) +' '+ lista[element])
            rep = 0
    return contagem
#-------------------------------------------------------
def removePontuacao(entrada):
    pontuacao = ",,[,],'"
    for element in pontuacao:
        entrada = entrada.replace(element,' ')
    return entrada

dados = []

#importando dados de csv
with open ('actors.csv', 'r',encoding="utf-8") as actors:
    csv = actors.readlines()
    for lines in csv:
        dados.append(lines)

#print(dados)
data = []
#criando lista com cada linha
for lines in dados:
    if lines[0] == '"': ## tratando robert, jr
        pass # por enquanto robert, jr foi eliminado pois seu nome deu problema na filtragem por ","
    else:
        data.append(lines.split(",")) # separando por virgulas

data = data[1:] #removendo cabeçalho
#print(data)

listaFilmes = []
for lines in data:
    listaFilmes.append(lines[4])

saida = contaRep(listaFilmes)
#print(saida)
saida.sort()
saida = removePontuacao(str(saida[-1:]))
print(saida)

with open ('filme_mais_frequente.txt', 'w') as arquivo:
    arquivo.write(saida)