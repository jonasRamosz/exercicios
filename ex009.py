n1 = int(input('Digite Um Valor !'))
print('TABUADA DE {}'.format(n1))
print('=-'*8)
for i in range (1,11):
    soma = n1 * i
    print('{} x {:2} = {}   \t|'.format(n1,i,soma))
print('=-'*8)