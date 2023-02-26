# faça um programa que jogue par ou impar com o computador. o jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
print('=-=-=-=-=-=- VAMOS JOGAR PAR OU ÍMPAR =-=-=-=-=-=-')
v = 0
while True:
    player = int(input('Degite um valor: '))
    comp = randint(0, 10)
    total = player + comp
    parouimp = ' '
    while parouimp not in 'pi':
        parouimp = str(input('Par ou Ímpar? P|I: ')).lower().strip()[0]
    if parouimp == 'p':
        if total % 2 == 0:
            print(f'Você VENCEU! O computador escolheu {comp} e a soma deu {total}, que é PAR.')
            v += 1
        else:
            print(f'Que pena, você perdeu! O computador escolheu {comp} e a soma deu {total}, que é ÍMPAR.')
            break
    elif parouimp == 'i':
        if total % 2 != 0:
            print(f'Você VENCEU! O computador escolheu {comp} e a soma deu {total}, que é ÍMPAR.')
            v += 1
        else:
            print(f'Que pena, você perdeu! O computador escolheu {comp} e a soma deu {total}, que é PAR.')
            break
    print('\nVamos jogar de novo...')
print(f'''
GAME OVER.
Total de vitórias consecutivas: {v}.''')






