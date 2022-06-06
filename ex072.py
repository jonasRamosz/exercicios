numeros = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez'
n1 = 0
while True:

    while True:
        n1 = int(input('Digite um numero de 0 a 10 :'))
        if 0 <= n1 <= 10:
            break

    print(f'você digitou o numero {numeros[n1]}')

    pergunta = ' '
    while pergunta not in "SN":
        pergunta = str(input('Você deseja continuar ? [S/N]')).strip().upper()[0]

    if pergunta == 'N':
        break

print('ADEUS')