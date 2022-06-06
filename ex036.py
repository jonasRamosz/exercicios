print('\tBem vindo ao banco de liuye!!\n\tVamos ao sistema de financiamento mobiliario ')

nome = str(input('Digite o seu nome !'))
vcasa = float(input('Digite o valor da casa !'))
salario = float(input('Digite o valor do seu salario !'))
anos = int(input('Digite em quantos meses voce pretende pagar !'))

vparcela = vcasa/anos
por100salario = (salario*30) / 100
print('=-'*23)
if (vparcela <= por100salario):
    print('\tPARABENS SENHOR {}\n\tO seu financiamento foi aprovado !!'.format(nome.upper()))
    print('\tO valor Das parcelas seram de: {}R$'.format(vparcela))
    print('\tSerão um total de {} parcelas.'.format(anos))

else:
    print('Infelizmente o seu financiamento foi recusado !')
