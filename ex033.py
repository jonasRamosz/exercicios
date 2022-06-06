n1 = int(input('Digite um numero'))
n2 = int(input('Digite outro numero'))
n3 = int(input('Digite outro numero'))

if (n1 > n2) and (n3 > n2) and (n1 > n3):
    print('{} é o maior numero, {} é o menor numero'.format(n1,n2))

elif(n1 > n2) and (n3 > n2) and (n1 < n3):
    print('{} é o maior numero, {} é o menor numero'.format(n3,n2))


elif (n2 > n1) and (n3 > n1) and (n2 > n3):
    print('{} é o maior numero, {} é o menor numero'.format(n2,n1))

elif (n2 > n1) and (n3 > n1) and (n2 < n3):
    print('{} é o maior numero, {} é o menor numero'.format(n3,n1))


elif (n1 > n3) and (n2 > n3) and (n1 > n2):
    print('{} é o maior numero, {} é o menor numero'.format(n1,n3))

elif (n1 > n3) and (n2 > n3) and (n1 < n2):
    print('{} é o maior numero, {} é o menor numero'.format(n2,n3))