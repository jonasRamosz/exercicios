import random
x = 1

while x == 1:
    num = random.randint(0, 5)
    n1 = int(input('Digite um numero de 0 a 5 !'))

    if num == n1:
        print('PARABENS, Você acertou, o numero certo era {}'.format(num))
        x = 0

    else:
        print('Errou, Você escolheu o numero {}, era o errado, o numero certo era : {}'.format(n1,num))

print('Parabens, Ate a proxima ')
