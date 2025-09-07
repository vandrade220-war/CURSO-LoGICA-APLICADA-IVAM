
#fazer cadastro de aboilusno e notas colocar e uma lista e fazer a validação para cada aluno

alunoss = []
notass = []

while True:
   nome = input('qual nome do aluno')
   if nome == '-1':
       break
   notas = input('qual a nota do aluno')
   if notas == "-1":
       break
   alunoss.append(nome)
   notass.append(notas)

for i in range(len(alunoss)):
    print(f'O aluno é: {alunoss[i]} e sua nota é {notass[i]}')




