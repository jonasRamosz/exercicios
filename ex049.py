valor = 0
print('\tBem-Vindo\n\tTabuada automatica')
n1 = int(input('Digite o numore da tabuada que voce quer !'))
print('Você escolheu a tabuada de {}'.format(n1))
print('-='*22)
for x in range (1,11):
    valor = n1 * x

    print('{} X {} = {}'.format(n1,x,valor))
