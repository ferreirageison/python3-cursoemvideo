# faça um programa que ajude o jogador a criar palpites de jogo da mega-sena (1-60). perguntar quantos jogos serão gerados. cadastrar tudo em uma lista composta.
from random import randint
from time import sleep

# listas e váriaveis
sorteios = []
jogo = []
num = 0

print('-'*40)
print('JOGO DA MEGA')
print('-'*40)

# input
njogos = int(input('Deseja sortear quantos jogos?: '))

while len(sorteios) < njogos:
#sorteio de um jogo
    while len(jogo) < 6:
        num = randint(1, 60)
        if num not in jogo: # teste de duplicata
            jogo.append(num)
            jogo.sort() # ordena permanentemente os números
    sorteios.append(jogo[:])
    jogo.clear()

print(f'-=-=-=-=-< Sorteando {njogos} jogos >-=-=-=-=')
for p, j in enumerate(sorteios):
    sleep(0.5)
    print(f'Jogo {p + 1}: {j}')
sleep(0.5)
print(f'=-=-=-=-=-=-< BOA SORTE! >-=-=-=-=-=-=')
