#Crie uma classe chamada Animal. Metodo nome, tipo e emite o som

class Animal:
    def emitir_som(animal):
        pass

class Vaca(Animal):
    def emitir_som(vaca):
        print("Muuuuuuuu!!")

class Cachorro(Animal):
    def emitir_som(cachorro):
        print("Au au!!")

class Peixe(Animal):
    def emitir_som(peixe):
        print("Glub, Glub!!")

class Gato(Animal):
    def emitir_som(gato):
        print("Miau!!")

# Teste do exercício
animal = Animal()
animal.emitir_som()  

vaca = Vaca()
vaca.emitir_som() 

cachorro = Cachorro()
cachorro.emitir_som()  

peixe = Peixe()
peixe.emitir_som() 

gato = Gato()
gato.emitir_som() 

