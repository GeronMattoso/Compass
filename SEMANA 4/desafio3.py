#-----------------------------------------------------
# txt 3 - O ator/atriz com a maior média por filme.

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
averageMovies = []
for lines in data:
     averageMovies.append(float(lines[3]))

averageMovies.sort()
maiorEverage = averageMovies[-1:]
maiorEverage = maiorEverage[0]

for lines in data:#txt 1
    if (float(lines[3]) == maiorEverage):
        print(lines[0], lines[3])
        actor = lines[0]      
        everage = lines[3]

with open ('everage_por_autor.txt', 'w') as arquivo:
    arquivo.write(actor)
    arquivo.write(", ")
    arquivo.write(str(everage))