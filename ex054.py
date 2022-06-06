maior = 0
menor = 0

n1 = int(input('Digite o ano de nacimento da pessoa 1'))
n2 = int(input('Digite o ano de nacimento da pessoa 2'))
n3 = int(input('Digite o ano de nacimento da pessoa 3'))
n4 = int(input('Digite o ano de nacimento da pessoa 4'))
n5 = int(input('Digite o ano de nacimento da pessoa 5'))
n6 = int(input('Digite o ano de nacimento da pessoa 6'))
n7 = int(input('Digite o ano de nacimento da pessoa 7'))

ano = [n1,n2,n3,n4,n5,n6,n7]

for x in range(0,7):
    if ano[x] <= 1999:
        maior += 1
    else:
        menor += 1

print('\t{} pessoas já são estão na maioridade!!\n\t{} pessoas ainda são de menor!! '.format(maior,menor))