"""Implemente duas classes "Pato" e "Pardal" que herdem de uma classe "Passaro" a habilidade de "voar" e
"emitir som", porém, tanto "Pato" quanto "Pardal" devem emitir sons diferentes (de maneira escrita) no
console. Exemplo: Pato voa e faz “quack quack” e Pardal voa e faz “piu piu” """

class Passaro:
    def __init__(self, voa:bool):
        self.voa = voa
        self.som = "canta"

class Pato(Passaro):
    def __init__(self,  voa:bool,):
        super().__init__(voa)
        self.som = "quack quack"


class Pardal(Passaro):
    def __init__(self,  voa:bool):
        super().__init__(voa)
        self.som = "piu piu"



pato1 = Pato(False)
pardal1 = Pardal(True)

print(pato1.som)
print(pato1.voa)

print(pardal1.som)
print(pardal1.voa)