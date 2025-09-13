#13. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar
#outro valor deve aparecer valor inválido.



while True:

    num_semana = int(input(
        'Digite 1 para domingo, 2 para segunda, 3 para terça, 4 para quarta, 5 para quinta, 6 para sexta, 7 para sábado: '))
    if num_semana == 1:
        print('Domingo')
        break
    elif num_semana == 2:
        print('Segunda')
        break
    elif num_semana == 3:
        print('terça')
        break
    elif num_semana == 4:
        print('Quarta')
        break
    elif num_semana == 5:
        print('Quinta')
        break
    elif num_semana == 6:
        print('Sexta, O melhor dia, dia de abraçar a minha amada, te amo Isadora')
        break
    elif num_semana == 7:
        print('Sábado')
        break
    else:
        print('valor inválido')
