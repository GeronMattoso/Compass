#-----------------------------------------------------
# txt 2 - A média do número de filmes por autor. 

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
#-------------------------------------------------------

numMovietot = 0
count = 0
for lines in data:
    numMovietot += int(lines[2])
    count+=1

result = numMovietot/count
print(result)


with open ('media_num_filmes_por_ator.txt', 'w') as arquivo:
    arquivo.write(str(numMovietot/count))

