#19. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades
#do mesmo.

while True:

    numero = int(input('Digite um número menor que 1000: '))

    if numero > 1000:
        int(input('Digite um número abaixo que seja abaixo de 1000 mazanza'))
    else:
        if numero < 1000:
            centena = numero/100 
            dezena = numero/10
            break

print(f'Essa é a quantidade de centenas: {centena}, essa é a quantidade de dezenas: {dezena}, essa é a quantidade de unidades {numero}')
    


    