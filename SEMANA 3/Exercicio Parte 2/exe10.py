"""Implemente a classe Lampada. A classe Lâmpada recebe um booleano no seu construtor, True se a lâmpada
estiver ligada, False caso esteja desligada. A classe Lampada possuí os seguintes métodos:
• liga(): muda o estado da lâmpada para ligada
• desliga(): muda o estado da lâmpada para desligada
• esta_ligada(): retorna verdadeiro se a lâmpada estiver ligada, falso caso contrário
"""
class Lampada:
    def __init__ (self):
        self.ligada   = False
        self.desligada= True
        self.status   = False 

    def liga(self):
        if (self.status == True):
            print("A LAMPADA JA ESTA LIGADA!!")
        else:    
            print("LIGANDO")
            self.ligada = True
            self.desligada = False
            self.estaLigada()

    def desliga(self):
        if (self.status == False):
            print("A LAMPADA JA ESTA DESLIGADA!!")
        else:
            print("DESLIGANDO")
            self.ligada = False
            self.desligada = True
            self.estaLigada()

    def estaLigada(self):
        if self.status == True:
            self.status = False
        else:
            self.status = True



lampada1 = Lampada()
sair = 0
while(sair != 1):
    acao = int(input("\nLIGAR 1 \nDESLIGAR 2 \n"))
    
    if acao == 1: 
        lampada1.liga()
    elif acao == 2:
        lampada1.desliga()
    elif acao == 3:
        print("saindo...")
        sair = 1
    else:
        print("opcao errada!!")
        pass