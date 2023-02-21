# melhore o jogo do desafio 028 do Mundo 01, onde o computador vai "pensar" em um número entre 0 e 5. Só que agora, o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários.

from random import randint
from time import sleep
print('='*50)
print('Vou pensar em um número de 1 a 5.')
print('pensando...')
sleep(1)
print('pensando...')
sleep(1)
print('pensando...')
sleep(1)
print('Pronto!')
print('='*50)
player = 0
cont = 1
ia = randint(1, 5)  # usa o módulo para fazer o sorteio de números entre 1 e 5 e guarda na variável
player = int(input('Tente adivinhar em qual número eu pensei? '))
while player != ia:
    cont += 1
    print('='*50)
    player = int(input('ERRRRRROUUUU, tente de novo! '))
    print('='*50)
if cont == 1:
    print(f'Parabéns! Você é o bichão mesmo?! Acertou de primeira!')
elif cont > 1:
    print(
         f'Depois de {cont} tentativas, você acertou. O número {ia} foi o que eu pensei.')
    print('='*50)