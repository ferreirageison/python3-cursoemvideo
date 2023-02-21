# cálculo a área e quantidade de tinta para pintar (2 litros a cada m²)
l = float(input('Qual a largura da parede (me metros? '))
a = float(input('Qual a altura da parede (em metros)? '))
area = l * a
lt = area / 2
print('A área da sua parede é de {}m² e vai precisar de um total de {:.2f} litros de tinta para pintá-la'.format(area,lt))