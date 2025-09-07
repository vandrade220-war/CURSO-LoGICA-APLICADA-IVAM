#14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule
#a sua média. A atribuição de conceitos obedece à tabela abaixo:

#Entre 9.0 e 10.0 A
 #Entre 7.5 e 9.0 B
 #Entre 6.0 e 7.5 C
 #Entre 4.0 e 6.0 D
 #Entre 4.0 e zero E
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o
#conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.


Nota_1 = float(input('Digite a primeira nota? '))
Nota_2 = float(input('Digite a segunda nota: '))

media = ((Nota_1 + Nota_2)/2)
print(media)

if media >= 9 and media <= 10:
    print('aluno conceito A')
    print('APROVADO')
elif media > 7.5 and media <= 9:
    print('aluno conceito B')
    print('APROVADO')
elif media > 6 and dia <= 7.5:
    print('aluno conceito C')
    print('APROVADO')
elif media > 4 and media <= 6:
    print('aluno conceito D')
    print('REPROVADO')
elif media < 4 and media <= 0:
    print('aluno conceito E')
    print('REPROVADO')