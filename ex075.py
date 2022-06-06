n1 = (int(input('Digite o primeiro numero')),
      int(input('Digite o segundo numero')),
      int(input('Digite o terceiro numero')),
      int(input('Digite o quarto numero')))
print('Os valores digitados foram !')
print(n1)
print(f'O valor 9 apareceu {n1.count(9)} vezes')
if 3 in n1:
    print(f'O valor 3 foi digitado na posição {n1.index(3)+1}')
else:
    print('O valor 3 nao foi digitado')
print('Os valores pares são :', end = ' ' )
for x in n1:
    if x % 2 == 0:
        print(x, ',',end = ' ')