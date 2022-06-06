numeros = []

while True:
    n = int(input('Digite um valor !'))

    if n not in numeros:
        numeros.append(n)

    else:
        print(f'O numero {n} já foi digitado ! digite um outro numero')
        n = int(input('Digite um valor !'))
        if n not in numeros:
            numeros.append(n)

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Voçê deseja continuar ?')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Os numeros digitados foram {numeros}')
