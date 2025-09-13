#28. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

#           Até 5 Kg            Acima de 5 Kg
#File Duplo R$ 4,90 por Kg     R$ 5,80 por Kg
#Alcatra    R$ 5,90 por Kg     R$ 6,80 por Kg
#Picanha    R$ 6,90 por Kg     R$ 7,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não
#há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
#desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada
#pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total,
#tipo de pagamento, valor do desconto e valor a pagar

tipo_carne = input('Qual tipo de carne você quer levar: File Duplo (F), Alcantra (A), Picanha(P)').upper()

if tipo_carne == "F":
    kg = float(input('Quantos kilos de Filé Duplo você quer??\n'))
    if kg <= 5:
        valor_final = kg *4.90
    else:
        valor_final = kg * 5.80

if tipo_carne == "A":
    kg = float(input('Quantos kilos de Alcatra quer??\n'))
    if kg <= 5:
        valor_final = kg *5.90
    else:
        valor_final = kg * 6.80

if tipo_carne == "P":
    kg = float(input('Quantos kilos de picanha você quer??\n'))
    if kg <= 5:
        valor_final = kg *6.90
    else:
        valor_final = kg * 7.80

valor_final_cartao = input('Você possui o cartão tabajara? se "sim" (Y) use ele e ganhe 10% de desconto: ').upper()

if valor_final_cartao == 'Y':
    valor_final_desconto = valor_final - (valor_final*0.10)
    print(f'Essa é a quantidade de carne que você comprou {kg}, o tipo da carne {tipo_carne} e o preço {valor_final_desconto}')
else:
    print(f'Essa é a quantidade de carne que você comprou {kg}, o tipo da carne {tipo_carne} e o preço {valor_final}')