#verificar se um numero de 5#

numero=int(input("Digite um numero:"))

if (numero % 5==0):
    print("esse numero é multiplo de 5.")
elif (numero % 2==0):
    print("esse numero é multiplo de 2.")
elif (numero % 3==0):
    print("esse numero é multiplo de 3")
else:
    print("esse numero nao é multiplo de 5.")
