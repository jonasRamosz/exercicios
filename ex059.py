x = 0
maior = 0

n1 = int(input('Digite o primeiro numero!'))
n2 = int(input('Digite o segundo numero!'))

while x == 0 :
    print('-='*20)
    print('------BEM VINDO-----')
    print('MENU CALCULADORA JONAS RAMOS')
    print('Digite [1] para somar!')
    print('Digite [2] para multiplicar')
    print('Digite [3] para maior numero entre os digitados')
    print('Digite [4] para digitar novos numeros')
    print('Digite [5] para sair do programa')
    a = int(input('Digite o Numero para a função !'))

    if a == 1:
        print('A soma dos numeros é {}'.format(n1 + n2))

    if a == 2:
        print('A multiplicação dos numeros é {}'.format(n1 * n2))
    if a == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior numero é: {}'.format(maior))
    if a == 4:
        n1 = int(input('Digite o primeiro numero!'))
        n2 = int(input('Digite o segundo numero!'))
    if a == 5:
        x = 1

