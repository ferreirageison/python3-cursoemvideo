# crie um programa onde 4 jogares joguem um dado e tenham resultados aleatórios entre 1 e 6. guarde esses resultados em um dicionário. no final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior númro no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogadores = {'Jogador 1': randint(1, 6),
             'Jogador 2': randint(1, 6),
             'Jogador 3': randint(1, 6),
             'Jogador 4': randint(1, 6)}

for k, v in jogadores.items():
    print(f'O {k} rolou os dados e tirou {v}')
    sleep(0.5)
print('-=-=-=-=-=-< Ranking dos jogadores: >-=-=-=-=-=-')

# ranking = sorted(jogadores.items(), key=lambda x: x[1], reverse=True)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for i, (k, v) in enumerate(ranking):
    print(f'{i+1}º lugar: {k} com {v}')
    sleep(0.5)

 