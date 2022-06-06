import random
cont = 0

while True:
    num = random.randint(1,10)
    print('Vamos jogar Ipar ou Par')
    print('-='*20)
    n1 = int(input('Digite um valor!'))
    va = str(input('Par ou Impar ? [P/I]')).strip().upper()

    if va == 'P':
        if ((n1 + num) % 2) == 0:
            print('Você venceu parabens !')
            print(f'Voce escolheu {n1} e a maquina escolheu {num}, Total de {n1 + num} DEU PAR')
            cont += 1

        if ((n1 + num) % 2) == 1:
            print('VOCE PERDEU !')
            print('=-'*15)
            print(f'Voce escolheu {n1} e a maquina escolheu {num}, Total de {n1 + num} DEU IMPAR')
            print(f'Voçê venceu {cont} vezes ! PARABENS')
            break


    if va == 'I':
        if ((n1 + num) % 2) == 1:
            print('Você venceu parabens !')
            print(f'Voce escolheu {n1} e a maquina escolheu {num}, Total de {n1 + num} DEU IMPAR')
            cont += 1

        if ((n1 + num) % 2) == 0:
            print('VOCE PERDEU !')
            print('=-' * 15)
            print(f'Voce escolheu {n1} e a maquina escolheu {num}, Total de {n1 + num} DEU PAR')
            print(f'Voçê venceu {cont} vezes ! PARABENS')
            break
