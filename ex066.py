cont = 0
soma = 0

while True:
    n1 = int(input('Digite valores (999 para parar!)'))
    if n1 == 999:
        break
    cont += 1
    soma += n1

print('-='*20)
print(f'A soma dos {cont} valores é = {soma}')
