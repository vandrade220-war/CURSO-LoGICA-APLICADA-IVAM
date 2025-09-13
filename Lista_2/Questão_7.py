#7. Faça um Programa que leia três números e mostre o maior e o menor deles

num = []

for i in range(3):
    valor = int(input('digite três números: '))
    num.append(valor)

maior_num = max(num)
menor_num = min(num)

print(f' esse é o Maior número: {maior_num}')
print(f' esse é o Menor número: {menor_num}')