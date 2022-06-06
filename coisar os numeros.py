uni = 0
dec = 0
sepa = []

def linha():
    print('=-'*25)

unidade = ['um','dois','treis','quatro','cinco','seis','sete','oito','nove']
decena = ['dez','vinte','trinta','quarenta','ciquenta','sessenta','setenta','oitenta','noventa']

while True:
    n1 = str(input('Digite o valor \nDigite 0 para finalizar'))
    for x in n1 :
        sepa.append(int(x))

    if int(n1) >= 10 :
        print(f'{decena[sepa[0]-1]} e {unidade[sepa[1]-1]}')
        linha()
        sepa.clear()

    elif int(n1) == 0:
        break

    elif int(n1) <= 9:
        print(f'{unidade[sepa[0]-1]}')
        linha()
        sepa.clear()