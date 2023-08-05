#Crie uma classe chamada Aluno, que herda de Pessoa. Adicione um método chamado estudar, que imprime "Estou estudando."

class Pessoa:
    def __init__(pessoa, nome, idade):
        pessoa.nome = nome
        pessoa.idade = idade
    
    def imprimir_pessoa(pessoa):
        print("Nome: ",pessoa.nome)
        print("Idade: ", pessoa.idade)

class Aluno(Pessoa):
    def __init__(aluno, nome, idade, matricula):
        super().__init__(nome, idade)
        aluno.matricula = matricula

    def imprimir_aluno(aluno):
        print("Matricula: ",aluno.matricula)

# Teste do exercício

aluno = Aluno("Rafael", 25, "32145")
aluno.imprimir_pessoa()
aluno.imprimir_aluno()
print("Estou estudando.")


      