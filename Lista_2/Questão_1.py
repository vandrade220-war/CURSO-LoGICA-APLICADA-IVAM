# 1. Faça um programa que peça dois números e imprima o maior deles.

num = []

for i in range(2):
    valor = input('digite um número')
    num.append(valor)


maior_num = max(num)
print(maior_num)

