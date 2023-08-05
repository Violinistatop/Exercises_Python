class Pessoa:
    def __init__(pessoa, nome , idade, e_mail , endereço ):
        pessoa.nome = nome 
        pessoa.idade= idade 
        pessoa.e_mail = e_mail
        pessoa.endereço = endereço
    def imprimir_nome(pessoa):
        print("nome:", pessoa.nome)
        print("idade:" ,pessoa.idade)
        print("e_mail:", pessoa.e_mail)
        print("endereço:", pessoa.endereço)

# teste do exercicio
cliente01 = Pessoa ("allan", 28 , 'allancarlos_1995@hotmail.com', "vila ema")
cliente01.imprimir_nome ()#saida : nome : allan