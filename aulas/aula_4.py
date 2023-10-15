"""  Calculadora de IMC (Índice de Massa Corporal): Crie um programa que
calcule o IMC com base no peso e altura fornecidos pelo usuário. """

# exemplo 4
peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))
imc = peso / (altura ** 2)
print(f"Seu IMC é {imc:.2f}")
