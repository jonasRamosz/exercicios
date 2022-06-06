num = []
par = []
impar = []

while True:
    num.append(int(input('Digite um valor')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar ? [S \ N] ')).strip().upper()[0]
    if resp == 'N':
        break

for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)

num.sort()
par.sort()
impar.sort()

print('-='*30)
print('O conteudo geral é')
print(num)
print('-='*30)
print('Os numeros pares digitados foram !')
print(par)
print('-='*30)
print('Os numeros impares digitados foram !')
print(impar)
print('-='*30)
