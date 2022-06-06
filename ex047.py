print('Bem-Vindo(a) ao processador de numeros pares')
print('-='*22)
n1 = int(input('Digite o valor da janela a ser processada'))
print('-='*22)

for x in range(1,n1 + 1):
    if (x % 2) == 0 :
        print(x)