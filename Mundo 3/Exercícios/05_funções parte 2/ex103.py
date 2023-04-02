# crie um programa que tenha uma funçao chamada ficha(), q receba 2 parametros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo q algum dado nao tenha sido informado corretamente.

def ficha(n='<desconhecido>', g=0):
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


#programa principal
jogador = str(input('Nome do Jogador: ')).capitalize().strip()
gols = str(input(f'Número de Gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if jogador.strip() == '':
    ficha(g=gols)
else:
    ficha(jogador,gols)

