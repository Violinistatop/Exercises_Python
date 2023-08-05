# Crie uma classe cahamada Pessoa com um método chamado apresentar. O metodo apresentar deve imprimir "Olá, eu sou uma pessoa."

class Pessoa:
    def __init__(pessoa,nome, idade):
        pessoa.nome = nome
        pessoa.idade = idade

    def imprimir_pessoa(pessoa):
        print("Nome: ",pessoa.nome)
        print("Idade: ", pessoa.idade)
        print("Olá, eu sou uma pessoa !")

#Teste do exercício

humano = Pessoa("Cátia", 43)
humano.imprimir_pessoa()
    