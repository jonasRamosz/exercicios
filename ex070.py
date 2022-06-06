total = 0
a = 0
cont = 1
menor = 0
barato = ' '
print('BEM - VINDO')
print('MERCADINHO BOM PREÇO')

while True:
    print('-' * 20)
    nome = str(input('PRODUTO: ')).strip().upper()
    preco = float(input('VALOR :'))

    resp = ' '
    while resp not in 'SN':
        resp = str(input('DESEJA CONTINUAR ?  [S/N]')).strip().upper()[0]

    total += preco
    if preco >= 1000 :
        a += 1


    if cont == 1:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            barato = nome
            menor = preco
    if resp == 'N':
        break
    cont += 1

print(f'TOTAL : {total:.2f}')
print(f'{a} PRODUTOS CUSTAM MAIS DE 1000R$')
print(f'O PRODUTO MAIS BARATO FOI {barato}, CUSTANDO {preco:.2f}')


