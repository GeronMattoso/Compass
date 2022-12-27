"""Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.
Dica: leia a documentação do pacote json, link: https://docs.python.org/3/library/json.html"""

import json

def parsingJason(arqJson):
    with open(arqJson) as openedJson:
        dataParser = json.load(openedJson)

    return(dataParser) 

a = "person.json"

print(parsingJason(a))