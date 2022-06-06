lista = 'jonas', 'matheus', 'melanie', 'arroz', 'joaquim', 'abacaxi'

for x in lista:
    print(f'\nNa palavra {x} temos', end = ' ')
    for k in x:
        if k.upper() in 'AEIOU':
            print(k, end = ' ')
