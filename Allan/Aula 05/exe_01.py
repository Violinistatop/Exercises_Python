def calcular_quadrado():
    lado = int(input("digite o lado do quadrado"))
    print ( " a area do quadrado de lado" , lado , "é", lado * lado)


def calcular_perimetro_quadrado ():   
    lado = int(input("digite o lado do quadrado")) 
    print (" o perimetro do quadrado " , lado ,"é", lado *4 )


def area_retangolo ():
    base = int(input("digite a base  do  retangulo "))
    altura = int(input("digite a altura  do retangulo"))
    area = ((base*altura))
    print ( " A area do retangulo é ", area )
    


def calcula_area_triangulo ():
    base = int(input("digite a base do triângulo"))
    altura = int(input("digite a base altura  do triângulo"))
    area = (( base * altura) / 2) 
    print ("A area do triangulo é" ,area)

def perimetro_triangulo_equilatero():
    lado = int(input("digite o lado  do triângulo"))
    lado = int(input("digite o lado  do triângulo"))
    lado= int(input("digite o lado  do triângulo"))
    perimetro = ((lado+lado+lado))
    print("O perimetro do triangulo é", perimetro )
