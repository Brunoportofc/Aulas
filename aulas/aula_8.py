"""  Verificação de Número Primo: Crie um programa que verifique 
se um número fornecido pelo usuário é primo.  """

# exemplo 8
numero = int(input("Digite um número inteiro: "))
primo = True

if numero <= 1:
    primo = False
else:
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break

if primo:
    print(f"{numero} é um número primo")
else:
    print(f"{numero} não é um número primo")
