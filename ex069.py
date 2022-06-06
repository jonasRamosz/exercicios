a = 0
h = 0
m = 0

while True:
    print('Cadastre uma pessoa !')
    print('-='*20)

    idade = int(input('Qual a idade da pessoa ?'))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo da pessoa ? [M/F]')).strip().upper()[0]

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar ? [S/N]')).strip().upper()[0]

    if idade > 18:
        a += 1
    if sexo == 'M':
        h += 1
    if sexo == 'F' and idade < 20:
        m += 1

    if resp == 'N':
        break

print('-='*20)
print(f'{a} pessoas tem mais de 18 anos')
print(f'{h} homens foram cadastrados')
print(f'{m} mulheres tem menos de 20 anos')