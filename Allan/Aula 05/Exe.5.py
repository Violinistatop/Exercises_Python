# Exercício 5:
# Crie uma classe chamada `Triangulo` que tenha os atributos `base` e `altura`.
#  Crie um método para calcular a área do triângulo.


class Triangulo:
    pass
    """def __init__(triangulo,base , altura):
        triangulo.base= base
        triangulo.altura=altura"""
       

    def calcular_area (triangulo):
        base=int(input("digite a base:" ))
        altura=int(input("digite a altura:"))
        area = base * altura / 2
        print ("a area do triangulo é:", area)
       


Meutriangulo =Triangulo()
Meutriangulo.calcular_area()
