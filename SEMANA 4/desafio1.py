#-----------------------------------------------------
#txt 1 - O ator/atriz com maior número de filmes e o respectivo número de filmes. 

#importando dados de csv
with open ('actors.csv', 'r',encoding="utf-8") as actors:
    dados = actors.readlines()

#print(dados)
data = []

#criando lista com cada linha
for lines in dados:
        data.append(lines.split(",")) # separando por virgulas
    #print(lines)
data = data[1:] #removendo cabeçalh

# data[4][0] = data[4][0] + data[4][1]
# data[4].pop(1)
# print(data[4])
newData = []
for i in range(0, len(data)):
    if(len(data[i])>6): # tratando nomme com virgula no meio
        data[i][0] = data[i][0] + data[i][1]
        data[i].pop(1)
        newData.append(data[i])
    else:
        newData.append(data[i])

#-------------------------------------------------------
# encontrando o maor numero de filmes
# numMovies = []
# for lines in data:
#     numMovies.append(float(lines[2]))
# numMovies.sort()
# maior = numMovies[-1:] # ultimo numero de filmes da lista ordenada "maior"
# maior = maior[0] # maior ainda era lista foi nescessario extrair o elemento

# for lines in data: # maior é onde o elemento 2 é igual ao encontrado
#     if (float(lines[2]) == float(maior)):
#         print(lines[0], lines[2])

# with open ('ator_maior_num_filmes.txt', 'w') as arquivo:
#     arquivo.write(atorMaior)
#     arquivo.write(", ")
#     arquivo.write(numMaior)
