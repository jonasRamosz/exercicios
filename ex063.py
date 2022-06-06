x = 3
a = 0
b = 1

n1 = int(input('Digite quantos numeros você deseja da sequencia de fibonacci !'))
print('{} → {}'.format(a,b), end = '')

while x <= n1:
    c = a + b
    a = b
    b = c
    print(' → {} '.format(c), end = '')


    x += 1
print('→ FIM')