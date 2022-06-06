print('Bem-vindo ao conversor de temperatura s2000 !')
resposta = input('Digite c para converter celsius em fahrenheit\nf para converter fahrenheit em celsius')
res = resposta.upper()

if res == 'C':
    print('Opcão escolhida: Gruas Celsius !!')
    valor = float(input('Digite o valor da temperatura! '))
    fah = (valor * 9/5) + 32
    print('Os {:.2f} graus celsius convertidos para fahrenheit são: {:.2f}!'.format(valor,fah))
elif res == 'F':
    print('Opção escolhida: graus fahrenheit')
    valor = float(input('Digite o valor da temperatura! '))
    cel = (valor - 32) * 5/9
    print('Os {:.2f} graus fahrenheit convertidos para celsius são: {:.2f}!'.format(valor,cel))
else:
    print('ERRO')
print('Tenha um bom dia !\nE volte sempre')


