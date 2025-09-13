#26. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#a. Álcool:
#b. até 20 litros, desconto de 3% por litro
#c. acima de 20 litros, desconto de 5% por litro
#d. Gasolina:
#e. até 20 litros, desconto de 4% por litro
#f. acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de
#combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente
#sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

def calcular_valor(litros, tipo):
    preco_alcool = 1.90
    preco_gazoza = 2.50

    if tipo == "A":
        preco = preco_alcool * litros
        if litros < 20:
            desconto = 0.03
        else:
            desconto = 0.05
    elif tipo == "G":
        preco = preco_gazoza * litros
        if litros > 20:
            desconto = 0.04
        else:
            desconto = 0.06
    else:
        return None
    
    return preco * (1 - desconto)

litros = float(input("Quantos litros vai ai meu patrão??"))
tipo = input('Gazoza (G)?? ou Alcool (A)??')

valor = calcular_valor(litros, tipo)
print(f'O valor que você vai pagar é de : {valor}')
