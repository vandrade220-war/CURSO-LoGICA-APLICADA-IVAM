#6. Faça um Programa que leia três números e mostre o maior deles.

num = []

for i in range(3):
    valor = int(input('digite três números: '))
    num.append(valor)

maior_num = max(num)

print(maior_num)