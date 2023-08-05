##Escreva um programa que receba uma lista de numeros do usuario e restorna a quantidade de elementos pares presentes na lista %

numeros = input("digite uma lista de número com espaço").split()
numeros = [int (num) for num in numeros]
contagem = 0 
for num in numeros:
    if num % 2 == 0:
        contagem += 1
print("A quantidade de numeros pares é :", contagem)

