n1 = int(input('Digite um numero!'))
x = n1
fatorial = 1

while x > 0 :
    fatorial *= x
    x -= 1

print('O fatorial de {} é = {}'.format(n1,fatorial))