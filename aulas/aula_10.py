"""Jogo de Adivinhação: Crie um jogo em que o programa
escolhe um número aleatório e o usuário tenta adivinhar qual é."""

# exemplo 10
import random

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    tentativa = int(input("Adivinhe o número (entre 1 e 100): "))
    tentativas += 1

    if tentativa == numero_secreto:
        print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
        break
    elif tentativa < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")
