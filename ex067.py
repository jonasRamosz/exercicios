while True:
    print('=-'*19)
    n1 = int(input('Deseja ver a tabuada de qual valor ?'))
    print('-='*19)

    if n1 >= 1:
        for x in range(1,11):
            print(f'{n1} X {x} = {n1*x}')

    if n1 < 0:
        break

print('Tabuada finalizada')
print('volte sempre !')