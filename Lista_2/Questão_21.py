#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
#quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é#
#de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na
#máquina.
#a. Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de
#5 e uma nota de 1;
#b. Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas
#de 10, uma nota de 5 e quatro notas de 1.

saque = int(input('Digite o valor que tu qués mazanza: '))

while True:
    if saque > 600 or saque < 10:
        saque = int(input('Seu saque deve ser mais que 10 reais e menor que 600 reais'))
    else:
        if saque < 600 or saque > 10:
            notas100 = saque // 100
            saque %= 100

            notas50 = saque // 50
            saque %= 50

            notas10 = saque // 10
            saque %= 10

            notas5 = saque // 5
            saque %= 5

            notas1 = saque

            print("Notas fornecidas:")
            if notas100 > 0:
                print(f"{notas100} nota(s) de 100")
            if notas50 > 0:
                print(f"{notas50} nota(s) de 50")
            if notas10 > 0:
                print(f"{notas10} nota(s) de 10")
            if notas5 > 0:
                print(f"{notas5} nota(s) de 5")
            if notas1 > 0:
                print(f"{notas1} nota(s) de 1")
        