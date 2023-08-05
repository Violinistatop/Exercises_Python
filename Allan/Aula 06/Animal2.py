#Crie uma classe chamada Animal. Metodo nome, tipo e emite o som

class Animal:
    def __init__(self, nome,tipo,som):
        self.nome = nome
        self.tipo = tipo
        self.som = som

    def imprime_bicho(self):
        print ("A nome desse animal é: ", self.nome)
        print ("O tipo desse animal é: ", self.tipo)
        
    def emite_som(self):
        print ("O som que esse animal emite é: ", self.som)



meubicho = Animal("Maria Flor", "Lhasa apso", "Au Au!!")
meubicho.imprime_bicho()
meubicho.emite_som()