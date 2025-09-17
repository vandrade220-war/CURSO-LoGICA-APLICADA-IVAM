#19. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades
#do mesmo.

while True:

    numero = int(input('Digite um número menor que 1000: '))

    if 0 <= numero < 1000:
        centenas = numero // 100
        dezenas = (numero % 100) // 10 
        unidades = numero % 10 

        partes = []
        if centenas > 0:
            partes.append(f'{centenas} centena' + ("s" if centenas > 1 else''))
        if dezenas > 0:
             partes.append(f'{dezenas} dezenas' + ("s" if dezenas > 1 else''))
        if unidades > 0:
             partes.append(f'{unidades} unidades' + ("s" if unidades > 1 else''))

    print(f"{numero} = " + ", ".join(partes[:-1]) + (" e " if len(partes) > 1 else "") + partes[-1])
         
