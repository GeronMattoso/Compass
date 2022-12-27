"""Escreve uma função que recebe como parâmetro uma lista e retorna 3 listas: a lista recebida dividida em 3
partes iguais. Teste sua implementação
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]"""

def divLista(lista, n):
    for element in range(0, len(lista), n):
        yield lista[element:element + n]
    return lista
    
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13]

# para nao perder dados e ter saidas do msm tamanho
# foram colocados zeros até a lista ser divisiivel por 3
while(len(b)%3 != 0): 
    b.append("0")
bLen = int(len(b)/3)

listaDividida = list((divLista(b, bLen)))

print(listaDividida)