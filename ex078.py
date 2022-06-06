maior = 0
menor = 0
numeros = []
pomaior = 0
pomenor = 0

for x in range(0,5):

    numeros.append(int(input('Digite um numero !')))

for c in range(0,5):
    if c == 0 :
        maior = numeros[c]
        menor = numeros[c]
        pomaior = numeros.index(numeros[c])
        pomenor = numeros.index(numeros[c])
    elif numeros[c] > maior:
        maior = numeros[c]
        pomaior = numeros.index(numeros[c])
    elif numeros[c] < menor:
        menor = numeros[c]
        pomenor = numeros.index(numeros[c])

print(f'Os numeros digitados foram : {numeros}')
print(f'O maior numero da digitado foi {maior} na posição {pomaior + 1}')
print(f'O menor numero digitado foi {menor} na posição {pomenor + 1}')
