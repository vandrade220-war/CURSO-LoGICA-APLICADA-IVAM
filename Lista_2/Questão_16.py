#16. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá
#pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer
#pedir os demais valores, sendo encerrado;
#b. Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#d. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

import math


a = float(input("Digite o valor de a: "))

if a == 0:
    print("O valor de 'a' não pode ser zero. Isso não é uma equação do segundo grau.")
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    delta = b**2 - 4*a*c

    if delta < 0:
        print("A equação não possui raízes reais, pois o delta é negativo.")

    elif delta == 0:
        raiz = -b / (2*a)
        print(f"A equação possui apenas uma raiz real: {raiz:.2f}")

    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"A equação possui duas raízes reais: {raiz1} e {raiz2}")
