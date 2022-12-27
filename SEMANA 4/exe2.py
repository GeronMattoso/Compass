class Pessoa:
    def __init__(self, nome:str, id:int):
        self.__nome = nome.title()
        self.id = id

    def nome(self):
        return self.__nome
        
    def newName(self, nome):
        self.__nome = nome.title()

pessoa1 = Pessoa("cleiton junior", 202020892)

print(pessoa1.id)

print(pessoa1.nome())

pessoa1.newName("cleitin")

print(pessoa1.nome())
