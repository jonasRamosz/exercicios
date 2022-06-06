n1 = float(input('Digite o salario do funcionario'))

if n1 > 1250 :
    almento = (10 * n1) / 100
    salarioplus = n1 + almento
    print('O salario atual com almento de 10 % é : {}'.format(salarioplus))
else:
    almento = (15 * n1) / 100
    salarioplus = n1 + almento
    print('O salario atual com almento de 15% é : {}'.format(salarioplus))