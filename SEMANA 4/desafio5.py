#-----------------------------------------------------
#txt 5 - O Autor que foi mais bem pago.

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
# encontrando o maior gross
gross = []
for lines in data:
    gross.append(float(lines[1]))
gross.sort()
maior = gross[-1:] # ultimo gross lista ordenada "maior"
maior = maior[0] # maior ainda era lista foi nescessario extrair o elemento


for lines in data: # maior é onde o elemento 2 é igual ao encontrado
    if (float(lines[1]) == float(maior)):
        print(lines[0], lines[1])
        atorMaior = lines[0]
        maiorGross = lines[1]
    else:
        pass

with open ('ator_maior_num_filmes.txt', 'w') as arquivo:
    arquivo.write(atorMaior)
    arquivo.write(", ")
    arquivo.write(str(maiorGross))