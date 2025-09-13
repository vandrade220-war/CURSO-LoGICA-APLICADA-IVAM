#12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
#depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário
#Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os
#descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo
#abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

salario = float(input('Digite seu salário:   '))

if salario <= 900:
    print(f'seu salário bruto é de:  {salario}')
    desconto_sindicato = (salario*0.03)
    print(f'O desconto do sindicato é {desconto_sindicato}')
    desconto_FGTS = (salario*0.11)
    print(f'O desconto do FGTS é: {desconto_FGTS}')
    salario_desconto = salario - ((desconto_sindicato)+(desconto_FGTS))
    print(f'O salário líquido é: {salario_desconto}')

elif salario > 900 and salario <= 1500:
    print(f'seu salário bruto é de:  {salario}')
    desconto_IR = salario * 0.05
    print(f' Esse desconto do IR {desconto_IR}')
    desconto_sindicato = (salario * 0.03)
    print(f'O desconto do sindicato é {desconto_sindicato}')
    desconto_FGTS = (salario * 0.11)
    print(f'O desconto do FGTS é: {desconto_FGTS}')
    salario_desconto = salario - ((desconto_IR) + (desconto_sindicato) + (desconto_FGTS))
    print(f'O salário líquido é: {salario_desconto}')

elif salario > 1500 and salario <= 2500:
    print(f'seu salário bruto é de:  {salario}')
    desconto_IR = salario * 0.10
    print(f' Esse desconto do IR {desconto_IR}')
    desconto_sindicato = (salario * 0.03)
    print(f'O desconto do sindicato é {desconto_sindicato}')
    desconto_FGTS = (salario * 0.11)
    print(f'O desconto do FGTS é: {desconto_FGTS}')
    salario_desconto = salario - ((desconto_IR) + (desconto_sindicato) + (desconto_FGTS))
    print(f'O salário líquido é: {salario_desconto}')

elif salario > 2500:
    print(f'seu salário bruto é de:  {salario}')
    desconto_IR = salario * 0.20
    print(f' Esse desconto do IR {desconto_IR}')
    desconto_sindicato = (salario * 0.03)
    print(f'O desconto do sindicato é {desconto_sindicato}')
    desconto_FGTS = (salario * 0.11)
    print(f'O desconto do FGTS é: {desconto_FGTS}')
    salario_desconto = salario - ((desconto_IR) + (desconto_sindicato) + (desconto_FGTS))
    print(f'O salário líquido é: {salario_desconto}')
