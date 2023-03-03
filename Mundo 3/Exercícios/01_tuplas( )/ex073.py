# crie uma tupla com os 20 primeiros colocados do brasileirão, na ordem de colocação, depois mostre: a) 5 primeiros b) últimos 4 c) lista em ordem alfabética d) posição do time da chapecoense

times = ('Corinthians', 'São Paulo', 'Atlético-PR', 'Coritiba', 'Vasco', 'Flamengo', 'Chapecoense', 'Paisandu', 'Cruzeiro', 'Paraná Clube', 'Fluminense', 'Botafogo', 'Palmeiras', 'Internacional', 'Goiás', 'Fortaleza', 'America Mineiro', 'Bahia', 'Ceará', 'Gremio')
chapecoense = times.index('Chapecoense') + 1
print('-' * 60)
print(f'Cinco primeiros colocados: {times[:5]}')
print('-' * 60)
print(f'Ultimos quatro colocados: {times[-4:]}')
print('-' * 60)
print(f'Ordem alfabética de times: {sorted(times)}')
print('-' * 60)
print(f'Posição do Chapecoense: {chapecoense}º')