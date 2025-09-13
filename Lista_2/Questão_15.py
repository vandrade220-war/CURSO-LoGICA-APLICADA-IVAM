#15. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um
#triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;

X = float(input('digite um valor para o primeiro lado: '))
Y = float(input('digite um valor para o segundo lado: '))
Z = float(input('digite um valor para o Terceiro lado: '))

if X == Y and Z == Y and X == Z:
    print('triangulo equilátero')
elif X == Y or X == Z or Y == Z:
    print('Triangulo isóceles')
elif X != Y and X != Z and Y != Z:
    print('triangulo escaleno')