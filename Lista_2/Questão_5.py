#5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a 7;
#A mensagem "Reprovado", se a média for menor do que 7;
#A mensagem "Aprovado com Distinção", se a média for igual a 10

nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('digite a segunda nota: '))

media = (nota_1 + nota_2)/2
print(f' sua média é: {media}')

if media == 10:
    print('Aprovado com Distinção')
elif media > 7:
    print('Aluno Aprovado')
else:
    print('Aluno reprovado')
