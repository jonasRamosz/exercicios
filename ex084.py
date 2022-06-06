pessoas = []
dado = []
contador = 0
mais = ' '

while True:
     dado.append(str(input('Nome : ')))
     dado.append(float(input('Peso :')))
     pessoas.append(dado[:])

     next = ' '
     while next not in 'SN':
         next = str(input('Deseja continuar ?')).strip().upper()[0]

     contador += 1
     if contador == 1 :
         mais = dado[1]
         menos = dado[1]

     else:
         if mais < dado[1]:
             mais = dado[1]

         elif menos > dado[1]:
             menos = dado[1]
     dado.clear()
     if next == 'N':
         break

print(f'O numero de pessoas cadastradas foram {len(pessoas)}')
for x in pessoas:
    if x[1] == mais:
        print(f'O mais pesado é {x[0]} com {mais:.2f}KG')
for a in pessoas:
    if a[1] == menos:
        print(f'O mais leve é {a[0]} com {menos:.2f}KG')
