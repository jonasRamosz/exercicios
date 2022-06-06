numeros = []
while True:
    numeros.append(int(input('Digite um numero')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar ? [S \ N]')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Foram digitados um total de {len(numeros)} na lista')

numeros.sort(reverse=True)
print(numeros)

if 5 in numeros:
    print('O 5  esta na lista')
else:
    print('O 5 NAO esta na lista')
