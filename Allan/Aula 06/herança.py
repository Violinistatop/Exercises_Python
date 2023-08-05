#Exercício 1: Crie uma classe chamada `Pessoa` que tenha o atributo `nome`. cadastro de pessoas, lista de pessoas, exibir pessoas


class Pessoa:
    def __init__(self):
        self.lista_pessoas = []
        self.lista_idades = []
        self.lista_emails = []

    def adicionar_pessoa(self):
        pergunta = int(input("Quantas pessoas deseja cadastar: "))
        for i in range (pergunta):
            self.lista_pessoas.append(input("Digite um nome para cadastrar: "))
            self.lista_idades.append(int(input("Digite um idade para cadastrar: ")))
            self.lista_emails.append(input("Digite uma email para cadastrar: "))
            i += 1

    def exibir_pessoas(self):
         for pessoa, idade, email in zip(self.lista_pessoas, self.lista_idades, self.lista_emails):
            print("Nome:", pessoa)
            print("Idade:", idade)
            print("Email:", email)
            print()
           
  
      
#Teste do exercício

p = Pessoa() # Criar uma instância da classe Pessoa

p.adicionar_pessoa() # Adicionar pessoas à lista

p.exibir_pessoas() # Exibir as pessoas na lista
