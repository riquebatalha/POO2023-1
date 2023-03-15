class Mago: # criando a classe Mago, onde foi colocado o construtor da classe (__init__)
    def __init__(self, nome, idade, escola, feitico, ferramenta):
        # Atributos e instâncias
        self.nome = nome
        self.idade = idade
        self.escola = escola
        self.feitico = feitico
        self.ferramenta = ferramenta

    def andar(self): # função simples com apenas um print
        print('Estou andando.')
    
    def falar(self): # função dando nome, idade e escola
        print('Prazer, meu nome é {}, tenho {} anos e estudo na escola de {}'.format(self.nome, self.idade, self.escola))
    
    def invocarMagia(self): # função simples com apenas um print
        print('Estou invocando a magia.')

    def usarFeitico(self): # função mostrando a magia do mago/a 
        print('O feitiço preferida do/a mago/a {} é a/o {}'.format(self.nome, self.feitico))

    def usarFerramenta(self): # função mostrando a ferramenta preferida
        print('A ferramenta preferida do/a mago/a {} é a/o {}'.format(self.nome, self.ferramenta))


if __name__ == '__main__':
    nome = str(input('Informe o seu nome: '))
    idade = float(input('Informe a sua idade: '))
    escola = str(input('Informe a sua escola: '))
    feitico = str(input('Informe o feitiço do mago/a: '))
    ferramenta = str(input('Informe a ferramenta do mago/a: '))
    m = Mago(nome,idade,escola,feitico,ferramenta)
    print('+=' * 18)
    m.andar()
    m.falar()
    m.invocarMagia()
    m.usarFeitico()
    m.usarFerramenta()
 

