class Cachorro:
    def __init__(meucachorro, nome , raça):
        meucachorro.nome = nome
        meucachorro.raça = raça
    
    def imprime_nome(meucachorro):
        print( "nome:" ,meucachorro.nome)
        print("Sua raça é: ", meucachorro.raça)


  
dog = Cachorro( "Princesa", "box")
dog.imprime_nome()