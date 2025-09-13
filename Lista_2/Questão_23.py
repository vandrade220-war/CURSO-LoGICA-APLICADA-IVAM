#23. Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de
#arredondamento.

numero = float(input('digite um número: '))

if numero == round(numero):
    print('é um número inteiro')
else:
    print('é um decimal')