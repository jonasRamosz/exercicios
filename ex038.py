n1 = int(input('Digite o primeiro numero !'))
n2 = int(input('Digite o segundo numero !'))

if n1 > n2 :
    print('O primeiro numero {} é maior que o segundo numero {} '.format(n1,n2))

elif n2 > n1 :
    print('o segundo numero {} é maior que o primeiro numero {}'.format(n2,n1))

else:
    print('Os dois numeros sao iguais !')