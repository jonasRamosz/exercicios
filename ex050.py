soma = 0

n1 = int(input('Digite um numero'))
n2 = int(input('Digite um numero'))
n3 = int(input('Digite um numero'))
n4 = int(input('Digite um numero'))
n5 = int(input('Digite um numero'))
n6 = int(input('Digite um numero'))

numeros = [n1,n2,n3,n4,n5,n6]

for x in range(0,6):
    if (numeros[x] % 2) == 0:
        soma = soma + numeros[x]
print('A soma dos pares é :{}'.format(soma))