cont = 0
n1 = int(input('Digite um numero !'))

for x in range (1,n1 + 1):

    if (n1 % x) == 0:
        cont += 1

if cont == 2:
    print('o numero {} é primo !!'.format(n1))
else:
    print('O numero {} nao é um numero primo !!'.format(n1))
    