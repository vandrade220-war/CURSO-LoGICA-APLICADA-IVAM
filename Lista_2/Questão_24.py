#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da
#operação deve ser acompanhado de uma frase que diga se o número é:
#a. par ou ímpar;
#b. positivo ou negativo;
#c. inteiro ou decimal.

numero1 = int(input('digite um número: '))
numero2 = int(input('digite um número: '))


escolha = input('qual operação você deseja fazer: 1 para soma, 2 para divisão, 3 para subtração, 4 para multiplicalção')

if escolha == "1":
    soma = numero1 + numero2
    print(f'esse é o resultado da soma: {soma}')
elif escolha == "2":
    divisao = numero1/numero2
    print(f'esse é o resultado da divisão: {divisao}')
elif escolha == "3":
    subtracao = numero1 - numero2 
    print(f'Esse é o valor da subtração {subtracao}')
elif escolha == "4":
    multiplica == numero1 * numero2 
    print(f'esse é2 o valor da multiplicação {multiplica}')