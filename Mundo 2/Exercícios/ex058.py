# melhore o jogo do desafio 028 do Mundo 01, onde o computador vai "pensar" em um número entre 0 e 5. Só que agora, o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários.

from random import randint
from time import sleep

print('Vou pensar em um número de 1 a 10, tente adivinhar...')
print('Pensando...')
sleep(1)

compute = randint(1,10)
player = 0
cont = 0

while player != compute:
    cont += 1
    player = int(input('Em qual número eu pensei? '))
    if player > compute:
        print('Um pouco menos...')
    else:
        print('Um pouco mais...')
if cont == 1:
    print('Acertou de primeira!!!')
else:
    print(f'Depois de {cont} tentativas, finalmente você acertou.')