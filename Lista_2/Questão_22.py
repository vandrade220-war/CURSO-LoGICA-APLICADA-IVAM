
#22. Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da
#divisão).

numero = int(input('digita um número ai que eu vou te dizer se ele é par ou impar'))

par_impar = numero % 2

if par_impar == 0: 
    print('número é par')
else:
    print('número é impar')