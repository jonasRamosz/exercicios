n1 = int(input('Digite em qual ano voce esta !'))

if (n1 % 4 == 0 and n1 % 100 != 0) or (n1 % 400 == 0):
    print('é bissexto')

else:
    print('Nao é bissexto')