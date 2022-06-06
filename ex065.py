x = 0
a = 0
media = 0
soma = 0
maior = 0
menor = 0
ask = ''

while x == 0:

    n1 = int(input('Digite um valor !'))
    ask = str(input('Você deseja continuar ? [S/N] ')).upper()

    if a == 0:
        maior = n1
        menor = n1

    if n1 > maior:
        maior = n1

    if n1 < menor:
        menor = n1

    if ask == 'N':
        x = 1

    a += 1
    soma += n1

media = soma/a
print('A media entre os numeros digitados é: {:.2F}'.format(media))
print('O maior numero digitado é: {}'.format(maior))
print('O menor numero digitado é: {}'.format(menor))
