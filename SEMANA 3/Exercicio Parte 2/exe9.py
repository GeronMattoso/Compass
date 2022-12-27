"""Escreva uma função que recebe um número variável de parâmetros não nomeados e um número variado de
parâmetros nomeados e imprime o valor de cada parâmetro recebido."""

def my_function(*args, **kargs):
    for item in args:
        print (item)
    for item in kargs:
        print (item)

my_function(1,2,3,55, "batata", nome="joao", teste="false")