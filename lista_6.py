class Assinatura:
    def calcular_preco(self):
        pass

    def exibir_detalhes(self):
        pass


class AssinaturaSimples(Assinatura):
    def calcular_preco(self):
        return 29.99

    def exibir_detalhes(self):
        print("Assinatura Simples: Acesso a filmes e séries em qualidade padrão.")


class AssinaturaPremium(Assinatura):
    def calcular_preco(self):
        return 49.99

    def exibir_detalhes(self):
        print("Assinatura Premium: Acesso a filmes e séries em qualidade HD e Ultra HD.")

assinatura_simples = AssinaturaSimples()
assinatura_premium = AssinaturaPremium()

assinaturas = [assinatura_simples, assinatura_premium]

for assinatura in assinaturas:
    tipo = assinatura.__class__.__name__
    preco = assinatura.calcular_preco()

    print("Tipo de Assinatura:", tipo)
    print("Preço: R$", preco)
    assinatura.exibir_detalhes()
    print()


class UnidadeMilitar:
    def mover(self):
        pass

    def atacar(self):
        pass


class Soldado(UnidadeMilitar):
    def mover(self):
        print("Soldado - Ataquei com a espada")
    
    def atacar(self):
        print("Soldado - Estou me movendo correndo")


class Arqueiro(UnidadeMilitar):
    def mover(self):
        print("Arqueiro - Ataquei com o arco")
    
    def atacar(self):
        print("Arqueiro - Estou me movendo silenciosamente")


class Cavaleiro(UnidadeMilitar):
    def mover(self):
        print("Cavaleiro - Ataquei com o machado")
    
    def atacar(self):
        print("Cavaleiro - Estou me movendo a cavalo")


unidades = [Soldado(), Arqueiro(), Cavaleiro()]

print('Batalha Medieval')
print('🏰 · ⚔️ · 🛡️ · ⚜ · 👑 · 🗡️ · 🏹 · 🕯️\n')
for unidade in unidades:
    unidade.mover()
    unidade.atacar()
    print('')