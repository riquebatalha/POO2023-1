'''dapte o exercício de revisão (mini-spotify), proponto uma classe Musica. Quais seriam seus
atributos? Quais seriam alguns dos seus possíveis métodos? Como poderíamos representar uma
playlist?'''


class Musica():
    def __init__(self, nome_musica, genero, minutos):
        self.nome_musica = nome_musica
        self.genero = genero
        self.minutos = minutos

    def tocar(self):
        print('A música que está tocando é: {}'.format(self.nome_musica))

    def saber_genero(self):
        print('O gênero da sua música é {}'.format(self.genero))

    def saber_minutos(self):
        print('A sua música apresenta {} minutos'.format(self.minutos / 100))


if __name__ == '__main__':
    nome = str(input('Informe o nome da música: '))
    genero = str(input('Informe o gênero da música: '))
    minutos = int(input('Informe quantos minutos a música tem: '))
    m = Musica(nome, genero, minutos)
    m.tocar()
    m.saber_genero()
    m.saber_minutos()



        