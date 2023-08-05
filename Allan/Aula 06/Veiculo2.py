# Exercício 1: Crie uma classe base chamada `Veiculo` com o atributo 

class Veiculo:
    def __init__(veiculo, marca,modelo,cor):
        veiculo.marca = marca
        veiculo.modelo = modelo
        veiculo.cor = cor

    def imprime_veiculo(veiculo):
        print ("A marca desse veículo é: ", veiculo.marca)
        print ("O modelo desse veículo é: ", veiculo.modelo)
        print ("A cor desse veículo é: ", veiculo.cor)
    
    def acelerar(veiculo):
        print ("O veiculo acelerou!!! Sai da frente!!! ")

meuveiculo = Veiculo("Jeep", "Renegade", "Vermelho")
meuveiculo.imprime_veiculo()
meuveiculo.acelerar()