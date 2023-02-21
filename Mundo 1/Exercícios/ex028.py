# jogo de adivinhação de um número de 1 a 5
from random import randint
from time import sleep
print('='*50)
print('Vou pensar em um número de 1 a 5.')
print('pensando...\npensando...\npensando...')
print('Pronto!')
print('='*50)
ia = randint(1, 5)  # faz o sorteio de números entre 1 e 5 e guarda
player = int(input('Tente adivinhar em qual número eu pensei? '))
print('Processando...')
sleep(2) 
if player == ia:  # faz o teste de acerto
    print('='*50)
    print(
        f'Porra! Você é o bichão mesmo?! O número {ia} foi exatamente o que eu pensei.')
    print('='*50)
else:
    print('='*50)
    print(
        f'Faustão: ERRROUUUU! Você disse {player} e eu pensei no {ia}.')
    print('='*50)
