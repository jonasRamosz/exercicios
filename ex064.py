n1 = 0
soma = 0
a = 0

while n1 < 999 :
    n1 = int(input('Digite um numero inteiro'))
    if n1 < 999:
      soma += n1
      a += 1
        
print('-='*20)
print(f'A soma dos numeros digitados é : {soma}')
print(f'Foram digitados {a} numeros ')