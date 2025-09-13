#Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno
#e presentar:
#a. A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#b. A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#c. A mensagem "Aprovado com Distinção", se a média for igual a 10.

lista_notas = []


for i in range(3):
    nota = int(input('digite a nota do aluno'))
    lista_notas.append(nota)

    quantidade_notas = len(lista_notas)
    
    media = (sum(lista_notas) /quantidade_notas)


print(f'essa é a média do aluno {media}')

if media == 10:
    print('Aprovado com Distinção')
elif media > 7:
    print('Aluno Aprovado')
else:
    print('Aluno reprovado')


