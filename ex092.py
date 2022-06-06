from datetime import datetime
dados = {}
dados['nome'] = str(input('NOME :')).strip().upper()
nasc = int(input('ANO DE NASCIMENTO :'))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('CARTEIRA DE TRABALHO :  (DIGITE 0 CASO A PESSOA NAO TENHA UMA )'))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('ANO DE CONTRATAÇÃO :'))
    dados['salario'] = float(input('SALARIO :'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)

print(f'Nome : {dados["nome"]}')
print(f'idade :{dados["idade"]}')
print(f'Carteira de trabalho :{dados["ctps"]}')

if dados['ctps'] != 0:
    print(f'Ano de contratação :{dados["contratação"]}')
    print(f'Salario : {dados["salario"]:.2f}')
    print(f'Idade com que vai se aposentar :{dados["aposentadoria"]}')

