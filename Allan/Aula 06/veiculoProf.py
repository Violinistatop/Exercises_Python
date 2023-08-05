# Exercício 1: Crie uma classe base chamada `Veiculo` com o atributo `velocidade` e um método `acelerar()`. Crie uma classe derivada chamada `Carro` que também tenha o atributo `marca` e um método `ligar()`.

class Veiculo:
    def __init__(self, velocidade):
        self.velocidade = velocidade
    
    def acelerar(self):
        self.velocidade += 0

class Carro(Veiculo):
    def __init__(self, velocidade, marca):
        super().__init__(velocidade)
        self.marca = marca
    
    def ligar(self):
        print("Carro ligado")

# Teste do exercício
carro = Carro(299, "Porche")
carro.ligar() 
carro.acelerar()
print(f"A marca do carro é {carro.marca} e sua velocidade é de {carro.velocidade} Km/h.")

