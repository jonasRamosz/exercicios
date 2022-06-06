completo = []
lista = []
rendi = {}

while True:
    rendi.clear()
    rendi['nome'] = str(input('NOME :'))
    partidas = int(input(f'Quantas partidas {rendi["nome"]} jogou : '))
    lista.clear()
    for x in range(1,partidas +1):
        lista.append(int(input(f'quantos gols na partida {x} : ')))
    rendi['gol'] = lista[:]
    rendi['total'] = sum(lista)
    completo.append(rendi.copy())

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar ?')).strip().upper()[0]

    if resp == 'N':
        break
print('-'*30)
for k, v in enumerate(completo):
    print(f'{k+1:>4} ', end = ' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
        print()


print(completo)




















#print(rendi)
#print('-'*30)
#print(f'nome : {rendi["nome"]}')
#print(f'Gols por partida :{rendi["gol"]}')
#print(f'Total de gols :{rendi["total"]}')
#print('-'*30)
#print(f'O jogador {rendi["nome"]} jogou {partidas} partidas.')
#or i,v in enumerate(lista):
    #print(f'  Na partida {i+1} fez {v} gols')
#print(f'foi um total de {total} gols')