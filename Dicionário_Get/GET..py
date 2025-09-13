
texto = 'Eles estão estão de olho em nóis'
contagem = {}

for palavras in texto.split():
    contagem[palavras] = contagem.get(palavras,0) +1

print(contagem)

