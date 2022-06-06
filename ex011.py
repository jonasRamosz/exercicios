largura = float(input('\tDigite O Valor Da Largura Da Parede !'))
altura = float(input('\tDigite O Valor Da Altura Da Parede !'))
area = largura * altura
tinta = area/2
print('\tA Sua Parede possui {}m² De Largura e {}m² de altura! \n  \tA Area Da Parede é : {}m² sera necessário um total de {} litros de tinta para pinta-la!'.format(largura,altura,area,tinta) )
