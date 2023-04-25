class Pais:
    def __init__(self, codigo_iso, nome, populacao, dimensao):
        self.codigo_iso = codigo_iso
        self.nome = nome
        self.populacao = populacao
        self.dimensao = dimensao
        self.fronteiras = []

    def get_codigo_iso(self):
        return self.codigo_iso

    def set_codigo_iso(self, codigo_iso):
        self.codigo_iso = codigo_iso

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_populacao(self):
        return self.populacao

    def set_populacao(self, populacao):
        self.populacao = populacao

    def get_dimensao(self):
        return self.dimensao

    def set_dimensao(self, dimensao):
        self.dimensao = dimensao

    def adicionar_fronteira(self, pais):
        if pais not in self.fronteiras:
            self.fronteiras.append(pais)
            pais.fronteiras.append(self)

    def eh_limitrofe(self, outro_pais):
        return outro_pais in self.fronteiras

    def densidade_populacional(self):
        return self.populacao / self.dimensao

    def __eq__(self, outro_pais):
        if isinstance(outro_pais, Pais):
            return self.codigo_iso == outro_pais.get_codigo_iso()
        return False

    def vizinhos_comuns(self, outro_pais):
        vizinhos = []
        for pais in self.fronteiras:
            if pais in outro_pais.fronteiras:
                vizinhos.append(pais)
        return vizinhos

class Continente:
    def __init__(self, nome):
        self.nome = nome
        self.paises = []
    
    def adicionar_pais(self, pais):
        self.paises.append(pais)
    
    def dimensao_total(self):
        return sum(pais.dimensao for pais in self.paises)
    
    def populacao_total(self):
        return sum(pais.populacao for pais in self.paises)
    
    def densidade_populacional(self):
        return self.populacao_total() / self.dimensao_total()
    
    def pais_maior_populacao(self):
        return max(self.paises, key=lambda pais: pais.populacao)
    
    def pais_menor_populacao(self):
        return min(self.paises, key=lambda pais: pais.populacao)
    
    def pais_maior_dimensao(self):
        return max(self.paises, key=lambda pais: pais.dimensao)
    
    def pais_menor_dimensao(self):
        return min(self.paises, key=lambda pais: pais.dimensao)
    
    def razao_territorial(self):
        maior_dimensao = self.pais_maior_dimensao().dimensao
        menor_dimensao = self.pais_menor_dimensao().dimensao
        return maior_dimensao / menor_dimensao
    
pais1 = Pais("BR", "Brasil", 211049527, 8515767)
pais2 = Pais("US", "Estados Unidos", 331002651, 9826675)
pais3 = Pais("CA", "Canadá", 37589262, 9984670)

continente = Continente("América")

continente.adicionar_pais(pais1)
continente.adicionar_pais(pais2)
continente.adicionar_pais(pais3)
print('+=' * 38)
print("Dimensão total do continente:", continente.dimensao_total())
print("População total do continente:", continente.populacao_total())
print("Densidade populacional do continente:", continente.densidade_populacional())
print("País com maior população no continente:", continente.pais_maior_populacao().nome)
print("País com menor população no continente:", continente.pais_menor_populacao().nome)
print("País de maior dimensão territorial no continente:", continente.pais_maior_dimensao().nome)
print("País de menor dimensão territorial no continente:", continente.pais_menor_dimensao().nome)
print("Razão territorial do maior país em relação ao menor país:", continente.razao_territorial())
print('+=' * 38)