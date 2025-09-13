
#25. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#a. "Telefonou para a vítima?"
#b. "Esteve no local do crime?"
#c. "Mora perto da vítima?"
#d. "Devia para a vítima?"
#e. "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no
#crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4
#como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".


a = int(input('Já telefonou para vitima? (1 para sim 2 para não)'))
b = int(input('Esteve no local do crime? (1 para sim 2 para não)'))
c = int(input('mora perto da vítima? (1 para sim 2 para não)'))
d = int(input('devia para vitma? (1 para sim 2 para não)'))
e = int(input('já tabalhou com a vítma?(1 para sim 2 para não)'))

soma_numeros = 0

if a == 1:
    soma_numeros += 1 
if b == 1:
    soma_numeros += 1 
if c == 1:
    soma_numeros += 1 
if d == 1:
    soma_numeros += 1 
if e == 1:
    soma_numeros += 1

print(soma_numeros)

if soma_numeros == 2: 
    print('supeito!')
elif soma_numeros == 3 or soma_numeros == 4:
    print('Cúmplice')
elif soma_numeros == 5:
    print('Assasino')
else:
    print('Inocente')




