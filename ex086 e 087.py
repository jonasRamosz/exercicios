matriz = [[],[],[]]
ler = 0
c = 1
soma = 0
somab = 0
cont = 0
for x in range(0,9):
    ler = int(input('digite um numero para a matriz :'))
    if c >=1 and c <=3:
        matriz[0].append(ler)
    elif c >=4 and c <=6:
        matriz[1].append(ler)
    elif c >= 7 and c <=9:
        matriz[2].append(ler)
    c += 1
    soma += ler

for p in matriz[2]:
    somab += p

    maior = matriz[1][0]
    for h in range(0, 3):
        if maior < matriz[1][h]:
            maior = matriz[1][h]


for a in range(0,3):
    print(f'[{matriz[0][a]:^5}]', end = ' ')
print(' ')
for a in range(0,3):
    print(f'[{matriz[1][a]:^5}]', end = ' ')
print(' ')
for a in range(0,3):
    print(f'[{matriz[2][a]:^5}]', end = ' ')
print(' ')
print(f'A soma de todos os valores é {soma}')
print(f'A soma dos valores da terceira coluna é {somab}')
print(f'O maior valor da segunda linha é {maior}')
