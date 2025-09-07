#8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a
#decisão é sempre pelo mais barato.

produtos = {}

for i in range(3):
    produto = input('qual é produto?')
    valor = float(input('Qual é o valor desse produto?'))
    produtos[produto] = valor

mais_barato = min(produtos, key=produtos.get)

print(f' você deve comprar o mais barato {mais_barato} que custa {produtos[mais_barato]}')