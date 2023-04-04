"""Crie uma classe chamada Calculadora, com os métodos somar, subtrair, multiplicar e dividir dois
números. Cada um destes métodos recebe por parâmetro dois números reais e retorna o
resultado da operação com os dois números. Se houver divisão por zero, imprimir um aviso na
execução do método e retornar -1"""

class Calculadora():
    def __init__(self, numero1, numero2):
        self._numero1 = numero1
        self._numero2 = numero2

    def somar(self):
        return 'Resultado da soma:', self._numero1 + self._numero2
    
    def subtrair(self):
        return 'Resultado da subtração:', self._numero1 - self._numero2
    
    def multiplicar(self):
        return 'Resultado da multiplicação', self._numero1 * self._numero2

    def dividir(self):
        if self._numero1 == 0 or self._numero2 == 0:
            print('Não é possível fazer essa divisão.')
            return -1
        else:
            return 'Resultado da divisão', self._numero1 / self._numero2
        

if __name__ == '__main__':
    c = Calculadora(0,2)
    print(c.somar())
    print(c.subtrair())
    print(c.multiplicar())
    print(c.dividir())
     