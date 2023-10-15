"""Calculadora Simples: Crie um programa que permita ao usuário realizar 
operações matemáticas básicas, como adição, subtração, multiplicação e divisão."""

# exemplo
num1 = float(input("Digite o primeiro número: "))
operador = input("Digite o operador (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))

if operador == '+':
    resultado = num1 + num2
elif operador == '-':
    resultado = num1 - num2
elif operador == '*':
    resultado = num1 * num2
elif operador == '/':
    resultado = num1 / num2
else:
    resultado = "Operador inválido"

print("Resultado:", resultado)
