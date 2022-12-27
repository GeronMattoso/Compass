
class Aviao:
    def __init__(self, modelo:str, velocidade_max:float, capacidade:int):
        self.modelo = modelo 
        self.velocidade_max = velocidade_max
        self.cor = 'azul'
        self.capacidade = capacidade

avioes = []

qtdAviao = 3

for element in range(qtdAviao):
    modelo = input(f"Modelo do aviao {element+1} = ")
    velocidade_max = input(f"Velocidade maxima do aviao{element+1} = ")
    capacidade = input(f"Capacidade do aviao {element+1} = ")
    avioes.append(Aviao(modelo, velocidade_max, capacidade))

for element in range(qtdAviao):
    print(f"O avião de modelo {avioes[element].modelo} possui uma velocidade máxima de {avioes[element].velocidade_max},capacidade para {avioes[element].capacidade} passageiros e é da cor {avioes[element].cor}")