

biblioteca = {'harry potter': 10,
              'candonblé': 23,
              'biblia':20}

while True:


    livro = input('Digite o Título do Livro: ').lower()
    if livro == "-1":
        break

    unidades = biblioteca.get(livro)

    if livro in biblioteca:
        print(f' este livro está na biblio com: {unidades} disponíveis')
    else:
        cadastro = int(input('não temos esse livro, quantas unidades quer cadastrar'))
        biblioteca[livro] = cadastro

print(biblioteca)