n1 = str(input('Digite a sua expressão'))
pilha = []
for x in n1:
     if x == '(':
         pilha.append('(')
     elif x == ')':
         if len(pilha) > 0:
             pilha.pop()
         else:
             pilha.append('(')
             break

if len(pilha) == 0:
    print('Sua expressão esta valida !!')
else:
    print('Sua expressão esta errada')