boletim = []
cont = 0

while True:
    nome = str(input('NOME: ')).strip().upper()
    n1 = float(input('NOTA 1: '))
    n2 = float(input('NOTA 2: '))
    media = (n1 + n2) / 2
    boletim.append([nome,[n1,n2],media])
    cont += 1
    next = ' '
    while next not in 'SN':
        next = str(input('Deseja continuar ?')).strip().upper()[0]
    if next == 'N':
        break
print('=-'*30)
print(f'{"NO.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*30)

for i in range(0,cont):
    print(f'{i+1:<4}{boletim[i][0]:<10}{boletim[i][2]:>8}')

while True:
    aluno = int(input('Digite o numero conrrespondente ao aluno que deseja ver a nota ?   | DIGITE 999 PARA SAIR '))
    print(f'notas de {boletim[aluno - 1][0]} é : {boletim[aluno - 1][1]}')
    print('-'*30)
    if aluno == 999:
        break

