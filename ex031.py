print('Ola, passagens de onibus ')
n1 = float(input('Digite a distancia em kms da sua viagem !'))

if n1 <= 200:
    valor = n1 * 0.50
    print('O valor da viagem sera de {}'.format(valor))

else:
    valor = n1 * 0.45
    print('o valor da viagem sera de {}'.format(valor))