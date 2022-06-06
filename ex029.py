
print('AVISO !!!')
print('Radar de velocidade a frente velocidade maxima 80km/h !!')
print('=-'*28)

velocidade = int(input('Digite a velocidade do veiculo !'))

if velocidade > 80 :
    velosobra = velocidade - 80
    valormulta = velosobra * 7
    print('Você esta acima da velocidade permitida e sera multado em {:.2f}R$'.format(valormulta))