import random
x = 1
tentativas = 0

while x == 1:
    num = random.randint(1,10)
    n1 = int(input('Digite um numero entre 1 a 10: '))

    tentativas += 1

    if num == n1:
         print('parabens voce acertou, mas usou {} tentativas'.format(tentativas))
         x = 0
