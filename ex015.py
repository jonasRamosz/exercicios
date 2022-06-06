dia = int(input('Quantos dias o carro ficou alugado ?'))
km = float(input('Quantos km o carro rodou ?'))
somadia = dia * 60
somakm = km * 0.15
valor = somadia + somakm
print('O total a pagar é de R${:.2f}'.format(valor))
