lista = 'arroz', 3.00, 'caneta', 0.50 ,'costelinha de porco', 16.50,'detergente', 2.00
print('-'*62)
print('LISTAGEM DE PREÇOS'.center(50,))
print('-'*62)
for x in range(0,len(lista)):
    if x % 2 == 0:
        print(f'{lista[x]:.<50}', end='')
    else:
        print(f'R${lista[x]:> 10.2f}')
print('-'*62)