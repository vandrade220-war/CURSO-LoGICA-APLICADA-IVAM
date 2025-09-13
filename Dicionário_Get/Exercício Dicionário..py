#1. Peça ao usuário para digitar o nome de um produto.
#2 .Verifique em um dicionário de estoque (já definido no código) se o produto existe.
#3 .Caso exista, exiba a quantidade disponível.
#4. Caso não exista, exiba uma mensagem informando que o produto não foi encontrado.


estoque = { 'banana': 12,
            'maça': 8,
            'jaca': 9,
            'uva(cachos)': 12}

produtos = input('Digite o nome de um produto').lower()

#estoque['pessego'] = 12   #assim adicionamos!

estoque.setdefault('laranja', 12)

quantidade = estoque.get(produtos) #.get aqui serve para ver a quantidade de produtos que tem
if quantidade is None:
    add_frut = int(input('Essa fruta não tem, digite quantas frutas você quer adicionar:\n'))
    estoque[produtos] = add_frut
else:
    print(f' temos essa fruta "{produtos}": {quantidade}')

estoque_update = {'melão':10,
                  'Codorna':5}

estoque.update(estoque_update)

print(estoque)

