lista = []
dic = {}
cont = 0
soma = 0
media = 0
while True:
    dic['nome'] = str(input('NOME :')).strip().upper()
    dic['sexo'] = str(input('SEXO : [M:masculino/F:feminino]')).strip().upper()[0]
    dic['idade'] = int(input('IDADE :'))

    cont += 1
    soma += dic['idade']

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar ?  [S/N]')).upper()[0].strip()
    lista.append(dic.copy())
    if resp == 'N':
        break

media = soma / cont

print(lista)
print('-='*30)
print(f'Um total de {cont} foram cadastradas')
print(f'A media da idade do grupo é : {media:.2f}')
print('mulheres cadastradas! ')
for x in lista:
    if x['sexo'] == 'F':
        print(x['nome'], end = ' ')
        print(' ')

print('Pessoas acima da media')
for i in lista:
    if i['idade'] > media:
        print(i["nome"])


