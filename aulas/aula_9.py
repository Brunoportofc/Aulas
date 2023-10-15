"""   Contagem de Vogais e Consoantes: Crie um programa que conte o número 
de vogais e consoantes em uma frase fornecida pelo usuário.  """

# Resposta 9
frase = input("Digite uma frase: ")
vogais = 0
consoantes = 0

for letra in frase:
    if letra.isalpha():
        if letra.lower() in 'aeiou':
            vogais += 1
        else:
            consoantes += 1

print(f"Vogais: {vogais}")
print(f"Consoantes: {consoantes}")
