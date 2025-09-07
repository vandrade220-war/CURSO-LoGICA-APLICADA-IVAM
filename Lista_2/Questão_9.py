#9. Faça um Programa que leia três números e mostre-os em ordem decrescente.

numeros = []
num = []

for i in range(3):

    numeros = int(input('Digita 3 números ai: '))
    num.append(numeros)

num.sort(reverse=True)

print(f'Números da forma reversa: {num}')
