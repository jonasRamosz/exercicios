import random
from time  import sleep
lista = []
jogos = []

quant = int(input('Quantos jogos voce quer fazer ?'))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = random.randint(1,60)
        if num not in lista :
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*20)
for i,v in enumerate(jogos):
    print(f'O jogo {i+1} :{v}')
    sleep(1.5)

