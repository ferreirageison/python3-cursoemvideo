# aprimore o desafio 093 para que ele funcione com vários jogadores (999 para sair), incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogadores = []
jogador = {}
gols = []
while True:
    jogador['Nome'] = str(input('Nome do Jogador: ')).strip().capitalize()
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    gols.clear()
    for p in range(partidas):
        gols.append(int(input(f'    Quantos gols na {p+1}ª partida? ')))
    jogador['Gols'] = gols.copy()
    jogador['Total'] = sum(gols)
    jogadores.append(jogador.copy())
    while True:
        perg = str(input('Cadastrar outro jogador? [S/N] '))
        if perg in 'SsNn':
            break
        print('Erro! Digete apenas S ou N.')
    if perg in 'Nn':
        break

print('=-'*30)
print('Cod', end=' ')
for k in jogador.keys():
    print(f'{k:<15}', end='')
print()
for i, j in enumerate(jogadores):
    print(f'{i:>3}', end=' ')
    for v in j.values():
        print(f'{str(v):<15}', end='')
    print()
print('---'*10)

while True:
    perg2 = int(input('Ver resultados de qual jogador? (999 para sair) '))
    if perg2 == 999:
        break
    if perg2 >= len(jogadores):
        print(f'ERRO! Não existe jogador de código {perg2}!')
    else:
        print(f'-- Levantamento do jogador {jogadores[perg2]["Nome"]}: ')
        for i, g in enumerate(jogadores[perg2]["Gols"]):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('---'*10)
print('Finalizado')