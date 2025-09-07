
#dicionários

#empregados = {'01':['joão', 'Silva'],
              #'02':['maria','Cornélia'],
              #'03':['Demiurgo', 'Planeta']}
#adicionado ao dicionário
#empregados['04'] = ['josé','lima']
#Removendo do dicionário
#del empregados['01']

#print(len(empregados))
#print(type(empregados))
#print(empregados)

#numero_func = input('qual número do funcionário')
#nome = input('digite o nome de funcionário')

#o que se sobresai aqui é a chave do funcionário


#if empregados.get(numero_func):
#    print('funcionário já cadastrado')
#else:
#    empregados[numero_func] = [nome]

#print(empregados)


dias = {'Sex': 'Sexta-Feira','Seg':'Segunda-Feira', 'Ter': 'Terça-Feira', 'Qua': 'Quarta-Feria', 'Quin': 'Quinta-Feira'}

chaves = dias.keys()  #retorna as chaves.
#print(chaves)

#for C in chaves:
#    print(C)

#value = dias.values()  #retorna os valores das chaves
#for V in value:
#    print(V)

#dias.pop('Sex')  #remove um item pela chave.
#for item in dias.items():
#    print(item)

#dias_copy = dias
#dias_copy['Dom'] = 'Domingo'
#print(dias)

import copy

dias_copy = copy.deepcopy(dias)
dias_copy['Dom'] = 'Domingo'
print(dias)
print(dias_copy)
