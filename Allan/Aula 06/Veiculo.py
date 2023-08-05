# Exercício 1: Crie uma classe base chamada `Veiculo` com o atributo `velocidade` e um método `acelerar()`. Crie uma classe derivada chamada `Carro` que também tenha o atributo `marca` e um método `ligar()`.


class Veiculo:
    def __init__(carro, marca, modelo):
        carro.marca = marca
        carro.modelo = modelo
        carro.velocidade = 0

    def acelerar(carro, aumentar):
        carro.velocidade += aumentar

    def frear(carro, diminuir):
        carro.velocidade -= diminuir

    def imprimir_informacoes(carro):
        print(f"Marca: {carro.marca}")
        print(f"Modelo: {carro.modelo}")
        print(f"Velocidade: {carro.velocidade} km/h")

#Teste do exercício

meu_carro = Veiculo("Toyota", "Corolla")
meu_carro.acelerar(30)
meu_carro.imprimir_informacoes()

   
       