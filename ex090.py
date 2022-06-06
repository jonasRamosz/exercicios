alunos = {}

alunos['nome'] = str(input('NOME :')).strip().upper()
alunos['media'] = float(input(f'MEDIA DE {alunos["nome"] } :'))
if alunos['media'] >= 6:
    alunos['situaçao'] = 'APROVADO'
elif alunos['media'] < 6:
    alunos['situaçao'] = 'REPROVADO'

print(f'O nome é {alunos["nome"]}')
print(f'Media igual a {alunos["media"]:.2f}')
print(f'A situação é {alunos["situaçao"]}')