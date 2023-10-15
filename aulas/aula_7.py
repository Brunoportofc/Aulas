"""Fatorial de um Número: Crie um programa que calcule o
fatorial de um número inteiro não negativo fornecido pelo usuário. """

# exemplo 7
numero = int(input("Digite um número inteiro não negativo: "))
fatorial = 1
if numero < 0:
    print("Fatorial não definido para números negativos.")
elif numero == 0:
    print("O fatorial de 0 é 1")
else:
    for i in range(1, numero + 1):
        fatorial *= i
    print(f"O fatorial de {numero} é {fatorial}")
