preço = float(input('Informe O Valor Do Produto!'))
desconto = float(input('Informe O Valor De Desconto!'))
a = (preço * desconto) / 100
b = preço - a
print('O Valor Original é {}R$ e o total de desconto será {}%, logo o Valor Final Com Desconto será {:.2f}R$'.format(preço,desconto,b))