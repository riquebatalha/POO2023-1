"""Faça um programa que simule um "dado virtual". O dado deve ser modelado como uma classe,
possuindo apenas o número de faces e o método Rolar, que retorna o valor sorteado. O número
de faces deve ser definido na criação do objeto (construtor com parâmetro). Deve ser instanciado
um dado com 6, 8 e 12 faces no main(). Cada dado deve ser jogado 3 vezes e o resultado de cada
jogada deve ser impresso na tela. Não deve ser usado print dentro da classe"""

import random

class Dado():
    def __init__(self, numero_faces):
        self._numero_faces = numero_faces

    
    def Rolar(self):
        return random.randint(1,self._numero_faces)
    

if __name__ == '__main__':
    d6 = Dado(6)
    d8 = Dado(8)
    d12 = Dado(12)

    for i in range(3):
        print('Numero da jogada: ', i + 1)
        print('Dado de 6 faces = {}'.format(d6.Rolar()))
        print('Dado de 8 faces = {}'.format(d8.Rolar()))
        print('Dado de 12 faces = {}'.format(d12.Rolar()))


        
