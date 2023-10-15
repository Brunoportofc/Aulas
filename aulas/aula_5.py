"""  Contagem Regressiva: Crie um programa que realize uma contagem 
regressiva a partir de um número fornecido pelo usuário até zero. """

# exemplo 5
numero = int(input("Digite um número inicial: "))
while numero >= 0:
    print(numero)
    numero -= 1
