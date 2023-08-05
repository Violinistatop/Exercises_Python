#Criar Jogo da advinhação com interação do usuário.

import random

class JogoAdivinhacao:
    def __init__(self):
        self.numero_secreto = random.randint(1, 100)
        self.tentativas = 0
    
    def jogar(self):
        while True:
            palpite = int(input("Digite um número entre 1 e 100: "))
            self.tentativas += 1
            
            if palpite < self.numero_secreto:
                print("O número secreto é maior!")
            elif palpite > self.numero_secreto:
                print("O número secreto é menor!")
            else:
                print(f"Parabéns! Você acertou o número secreto em {self.tentativas} tentativas!")
                break

#Teste do exercício

jogo = JogoAdivinhacao()
jogo.jogar()