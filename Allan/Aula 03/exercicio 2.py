##Escreva um programa que recebe uma lista de Número do usuario e retorna o maior valor do elemento presente na lista ###

numeros = input("digite uma lista de número por espaço").split()
numeros = [int (num) for num in numeros]
maior = max(numeros)
