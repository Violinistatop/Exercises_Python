# Crie uma classe chamada `Carro` que tenha os atributos `marca`, `modelo` e `ano`. Crie um método para imprimir as informações do carro.


class Carro:
    def __init__ (carro,marca, modelo,ano):
        carro.marca = marca
        carro.modelo= modelo
        carro.ano =  ano 


    def imprimir_carro(carro):
        print("marca:",carro.marca)
        print("modelo:", carro.modelo)
        print("ano :",carro.ano)


Veiculo = Carro ( "peugeot" ,"207", "2009" )
Veiculo.imprimir_carro()
     