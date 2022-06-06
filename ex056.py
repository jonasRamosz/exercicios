idademedia = 0
idadesoma = 0
maioridadehomem = 0
maiornomehomem = ''
somatoriomulher = 0
for x in range (1,5):
    print('---- {}ª PESSOA !! ----'.format(x))
    nome = str(input('NOME: ')).upper().strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO: M/F')).upper()
    idadesoma =+ idade

    if x == 1 and sexo == 'M':
        maioridadehomem = idade
        maiornomehomem = nome

    elif sexo == 'M' and idade > maioridadehomem :
        maioridadehomem = idade
        maiornomehomem = nome

    elif sexo == 'F' and idade < 20 :
        somatoriomulher += 1

idademedia = idadesoma / 4
print('A media de idade do grupo é: {}'.format(idademedia))
print('O homem mais velho se chama: {}! '.format(maiornomehomem))
print('A sua idade é de :{}'.format(maioridadehomem))
print('Um total de {} mulher(es) possuem menos de 20 anos '.format(somatoriomulher))