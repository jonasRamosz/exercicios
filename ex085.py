principal = [[],[]]
secundaria = 0

for x in range(0,7):
    secundaria = int(input('Digite um valor'))
    if secundaria % 2 == 0 :
        principal[0].append(secundaria)
    else:
        principal[1].append(secundaria)
principal[0].sort()
principal[1].sort()
print(principal)
print(f'os numeros impares são: {principal[1]}')
print(f'Os numeros pares são: {principal[0]}')