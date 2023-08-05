# Exercício 5:Crie uma classe chamada `Triangulo` que tenha os atributos `base` e `altura`. Crie um método para calcular a área do triângulo.

class Triangulo:
    def __init__ (triangulo,base,altura):
        triangulo.base = base
        triangulo.altura = altura
        
    
    def imprimir_nome(triangulo):
        print("A área do triângulo é : ",triangulo.base * triangulo.altura/2)
        

#Teste do exercício

area = Triangulo(12,25)
area.imprimir_nome()