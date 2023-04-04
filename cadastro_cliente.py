"""
Crie uma classe CadastroCliente com os atributos nome, sobrenome, data de nascimento, email,
CPF e senha. Faça um pequeno programa que permita o cliente se cadastrar e depois consultar
seus dados. Para consultar seus dados, é necessário que ele faça o login com seu email e senha.
Se o cliente errar a senha 3x, o cadastro é bloqueado e ele não pode mais acessar
"""

class CadastroCliente:
    def __init__(self, nome, sobrenome, data_nascimento, email, cpf, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
        self.email = email
        self.cpf = cpf
        self.senha = senha
        self.num_tentativas = 0
        self.bloqueado = False

    def cadastrar(self):
        print("Cadastro de Cliente")
        self.nome = input("Digite seu nome: ")
        self.sobrenome = input("Digite seu sobrenome: ")
        self.data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
        self.email = input("Digite seu email: ")
        self.cpf = input("Digite seu CPF: ")
        self.senha = input("Digite sua senha: ")

    def login(self, email, senha):
        if self.email == email and self.senha == senha:
            print("Login realizado com sucesso!")
            self.num_tentativas = 0
        else:
            self.num_tentativas += 1
            if self.num_tentativas == 3:
                self.bloqueado = True
                print("Número de tentativas excedido. Seu cadastro foi bloqueado.")
            else:
                print("Email ou senha incorretos. Tente novamente.")

    def consultar_dados(self, opcao, valor, senha):
        if self.bloqueado:
            print("Seu cadastro foi bloqueado.")
        elif self.senha == senha:
            if opcao == 1 and self.email == valor:
                print("Nome:", self.nome)
                print("Sobrenome:", self.sobrenome)
                print("Data de Nascimento:", self.data_nascimento)
                print("Email:", self.email)
                print("CPF:", self.cpf)
            elif opcao == 2 and self.cpf == valor:
                print("Nome:", self.nome)
                print("Sobrenome:", self.sobrenome)
                print("Data de Nascimento:", self.data_nascimento)
                print("Email:", self.email)
                print("CPF:", self.cpf)
            else:
                print("Opção inválida ou dados incorretos.")
        else:
            print("Senha incorreta. Tente novamente.")

def main():
    cliente = CadastroCliente("", "", "", "", "", "")

    cliente.cadastrar()

    print(' TELA DE LOGIN \n')
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    cliente.login(email, senha)

    opcao = int(input("Digite de qual jeito você quer acessar seus dados -  (1 - Email / 2 - CPF): "))
    valor = input("Digite o valor que você escolheu: ")
    senha = input("Digite sua senha: ")
    cliente.consultar_dados(opcao, valor, senha)

if __name__ == "__main__":
    main()