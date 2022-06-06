import math
n1 = float(input('Informe o cateto oposto :'))
n2 = float(input('Informe o cateto adjacente :'))
hypo = math.hypot(n1,n2)
print('O comprimento da hipotenusa é :{:.2f}'.format(hypo))