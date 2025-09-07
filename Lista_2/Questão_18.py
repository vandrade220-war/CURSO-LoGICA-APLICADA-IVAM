#18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

from datetime import datetime

data = input('digite uma data no formato dd/mm/aaaa: ')

try:
    datetime.strptime(data, "%d/%m/%Y")
    print(f'essa {data} é valida')
except ValueError:
    print(f'A data {data} é invalida')