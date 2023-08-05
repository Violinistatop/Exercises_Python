numeros = input("digite uma lista de número com espaço").split()
numeros = [int (num) for num in numeros]
soma = 0
for elemento in numeros:
    soma += elemento

print(soma)




