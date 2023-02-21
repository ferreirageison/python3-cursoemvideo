from random import randint
from time import sleep

print(f'{" VAMOS JOGAR - JOKEN PO ":#^50}')

print(str(
    'Escolha sua arma enquanto eu escolho a minha:\n'
    '[0] Pedra\n'
    '[1] Papel\n'
    '[2] Tesoura\n'))
player = int(input('Digite: '))  # escolha do jogador
# lista de opções para escolha por posição
armas = ['Pedra', 'Papel', 'Tesoura']
ia = randint(0, 2)  # escolha da arma do computador por sorteio randômico

if player == 0 or player == 1 or player == 2:
    print('...JO!')
    sleep(1)
    print('...KEN!')
    sleep(1)
    print('...PO!!!')
    if ia == 0:  # pedra:
        if player == 0:  # pedra
            res = 'empata com'
            print(f'{" EMPATE ":=^40}')
        elif player == 1:  # papel
            res = 'derrota'
            print(f'{" VITÓRIA ":=^40}')
        elif player == 2:  # tesoura
            res = 'perde para'
            print(f'{" DERROTA ":=^40}')
    if ia == 1:  # papel:
        if player == 0:  # pedra
            res = 'perde para'
            print(f'{" DERROTA ":=^40}')
        elif player == 1:  # papel
            res = 'empata com'
            print(f'{" EMPATE ":=^40}')
        elif player == 2:  # tesoura
            res = 'derrota'
            print(f'{" VITÓRIA ":=^40}')
    if ia == 2:  # tesoura:
        if player == 0:  # pedra
            res = 'derrota'
            print(f'{" VITÓRIA ":=^40}')
        elif player == 1:  # papel
            res = 'perde para'
            print(f'{" DERROTA ":=^40}')
        elif player == 2:  # tesoura
            res = 'empata com'
            print(f'{" EMPATE ":=^40}')
    print(
        # pega a variavel armas e mostra o item que está na posição que o jogador escolheu entre 0 e 2
        f'Você escolheu: {armas[player]}\n'
        # pega a variavel armas e mostra o item que está na posição que o computador escolheu randomicamente entre 0 e 2
        f'Computador escolheu: {armas[ia]}\n'
        f'{armas[player]} {res} {armas[ia]}')
else:
    print('Opção inválida! Escolha novamente')
