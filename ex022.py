n1 = str(input('Digite seu nome completo: ! ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiusculo é :{}'.format(n1.upper()))
print('Seu nome em minuscula é :{}'.format(n1.lower()))
print('Seu nome tem ao todo {} letras'.format(len(n1) - n1.count(' ')))
print('Seu primeiro nome tem {} letras'.format(n1.find(' ')))

