lista = []
for c in range(0,5):
    n = int(input('Digite um valor'))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos <= lista[pos]:
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1

print('-='*20)
print(f'Os valores digitados em ordem foram {lista}')