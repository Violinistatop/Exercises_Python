#criar um código para gerar palpites da Mega-Sena baseado nos jogos anteriores. Para isso, precisaremos de um histórico dos resultados anteriores.

import random

def gerar_palpite(historico):
    numeros = list(range(1, 61))  # Gerar uma lista de números de 1 a 60
    palpite = []  # Inicializar uma lista vazia para o palpite

    while len(palpite) < 6:
        # Escolher um número aleatório da lista de números disponíveis
        numero = random.choice(numeros)

        # Verificar se o número já está no palpite
        if numero not in palpite:
            palpite.append(numero)

    palpite.sort()  # Ordenar os números em ordem crescente
    return palpite

historico = ([5, 10, 15, 20, 25, 30],[2, 4, 6, 8, 10, 12],[12, 18, 24, 30, 36, 42],[7, 14, 21, 28, 35, 42],[1, 3, 5, 7, 9, 11])

palpite = gerar_palpite(historico)
print(palpite)