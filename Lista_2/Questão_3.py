#3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input('Digite "F" para feminino, "M" para Masculino: ').upper()

if sexo == "F":
    print('Sexo Feminino')
elif sexo == "M":
    print('Sexo masculino')
else:
    print("Sexo inválido")



