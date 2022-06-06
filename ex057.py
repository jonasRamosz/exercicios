sexo = str(input('Digite o seu sexo ![MASCULINO/FEMININO] ')).strip().upper()[0]

while sexo not in 'MF':
    sexo = str(input('Dado invalido digite novamente o seu sexo!')).strip().upper()[0]

idade = int(input('Digite a sua idade '))

if sexo == 'M':
    sexo = 'MASCULINO'
else:
    sexo = 'FEMININO'
print('Dado computado com sucesso , seu sexo é {} e sua idade é {}'.format(sexo,idade))