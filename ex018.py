import math
n1 = float(input('Digite um angulo que deseja tirar: sin ,cos e tan: '))
print(' O angulo informado foi: {:.2f}\n o valor do sin é {:.2f}\n o valor do cos é: {:.2f}\n e o valor da tan é: {:.2f}'.format(n1,math.sin(math.radians(n1)),math.cos(math.radians(n1)),math.tan(math.radians(n1))))