class Data():
    def __init__(self, dia, mes, ano, nome_cidade = None):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.nome_cidade = nome_cidade

    def imprimirData(self):
        print('Dia {} do mês {} do ano de {}'.format(self.dia, self.mes, self.ano))
    
    def imprimirDataPorExtenso(self):
        print('Dia {} do mês {} do ano de {}, na cidade de {}'.format(self.dia, self.mes, self.ano, self.nome_cidade))

if __name__ == '__main__':
    d = Data(10, 'maio', 2004, 'São Leopoldo')
    d.imprimirData()
    d.imprimirDataPorExtenso()