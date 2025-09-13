
#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#        Até 5 Kg    Acima de 5 Kg
#Morango R$ 2,50 por Kg R$ 2,20 por Kg
#Maçã    R$ 1,80 por Kg R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um
#desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
#(em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

def calcular_morango(kg):
    if kg <= 5:
        preco = 2.50 * kg
    else: 
        preco = 2.20 * kg
    return preco

def calcular_maca(kg):
    if kg <= 5:
        preco = 1.80 * kg
    else:
        preco = 1.50 * kg
    return preco

def calcular_total(kg_morango, kg_maca):
    preco_morango = calcular_morango(kg_morango)
    preco_maca = calcular_maca(kg_maca)

    total = preco_maca + preco_morango
    peso_total = kg_maca + kg_morango

    if peso_total > 8 or total > 25:
        total *= 0.90

    return total

kg_morango = float(input('Quantos kg de morango tu quer??'))
kg_maca = float(input('quantos kg de maca tu quer??')) 

valor_final = calcular_total(kg_maca, kg_morango)

print(f'seu valor final é: {valor_final}')
    

