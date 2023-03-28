# crie um programa que gerencie o aproveitamento de um Nome de futebol. o programa vai ler o nome e quantas partidas ele jogou. depois vai ler a quantidade de gols feitos e cada partida. tudo deve ser guardado num dicionário, incluindo o total de gols feitos durante o compeonato.

jogador = {}
gols = []

jogador['Nome'] = str(input('Nome do Jogador: ')).strip().capitalize()
jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

for i in range(jogador['Partidas']):
    gols.append(int(input(f'    Quantos gols na {i+1}ª partida? ')))

jogador['Gols'] = gols 
jogador['Total'] = sum(gols)

#maneira1
print('=-'*30)
print(jogador)

#maneira2
print('=-'*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

#maneira3
print('=-'*30)
print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas.')
for i in range(jogador['Partidas']):
    print(f'    => Na {i+1}ª partida, fez {gols[i]} gols.')
print(f'Somando um total de {jogador["Total"]} gols.')