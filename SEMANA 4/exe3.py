class Calculo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def soma(self):
        return self.x + self.y
    
    def subtracao(self):
        return self.x - self.y
    

calculo1 = Calculo(19, -92)
calculo2 = Calculo(11111, 6767)

print(calculo1.soma())

print(calculo1.subtracao())

print(calculo2.soma())

print(calculo2.subtracao())
