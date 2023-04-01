# faça um programa que tenha uma funçao chamada contador(), que tenha 3 parametros: inicio, fim e passo, e realize a contagem. seu programa tem que realizar 3 contagens atraves da funçao criada: a) de 1 até 10, de 1 em 1. b) de 10 até 0, de 2 em 2.  c) uma contagem.
from time import sleep

def lin():
    print('='*30)

def contador(* num):
    if num[2] < 0:
        print(f'Contagem de {num[0]} até {num[1]} de {num[2]} em {num[2]}')
        for i in range(num[0], num[1], (num[2])):
            print(i, end=' ', flush=True)
            sleep(0.1)
        print(f'{num[1]} FIM!')

    elif num[0] < num[1]:
        print(f'Contagem de {num[0]} até {num[1]} de {num[2]} em {num[2]}')
        for i in range(num[0], num[1], num[2]):
            print(i, end=' ', flush=True)
            sleep(0.1)
        print(f'{num[1]} FIM!')

    elif num[0] > num[1]:
        print(f'Contagem de {num[0]} até {num[1]} de {num[2]} em {num[2]}')
        for i in range(num[0], num[1], -num[2]):
            print(i, end=' ', flush=True)
            sleep(0.1)
        print(f'{num[1]} FIM!')

lin()
contador(1, 10, 1)
lin()
contador(10, 0, 2)
lin()
print('Agora é sua vez!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)

