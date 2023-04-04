import random

class Competidor:
    def __init__(self, nome):
        self.nome = nome
        self.pos = 0

    def atualizar(self):
        dado = random.randint(1,6)
        self.pos += dado
        
        if self.pos % 5 == 0:
            self.pos -= 1
        elif self.pos == 7 or self.pos == 17:
            self.pos += 2
        elif self.pos == 13:
            self.pos = 0

    def getPos(self):
        return self.pos


competidores = [Competidor("Competidor " + str(i+1)) for i in range(5)]
corrida_terminada = False
vencedor = None

if __name__ == '__main__':
    competidores = [Competidor('João'), Competidor('Maria'), Competidor('Ana'), Competidor('Pedro'), Competidor('José')]
    vencedor = None
    
    while not vencedor:
        for competidor in competidores:
            competidor.atualizar()
            print(f'Competidor: {competidor.nome} | Posição: {competidor.getPos()}')
            
            if competidor.getPos() >= 20:
                vencedor = competidor
                break
        
        print()
    
    print(f'{vencedor.nome} venceu a corrida!')
    for competidor in competidores:
        if competidor != vencedor:
            print(f'{competidor.nome} | Posição: {competidor.getPos()}')
        else:
            print(f'{vencedor.nome} | Posição: {vencedor.getPos()}')