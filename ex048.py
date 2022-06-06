soma = 0

for x in range(1,501):
    if (x % 2) == 1:
        if (x % 3) == 0:
            soma = soma + x

print('A soma de todos os numeros impares divisiveis por 3 é : {}'.format(soma))
