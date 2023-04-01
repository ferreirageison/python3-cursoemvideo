# faça um programa que tenha uma funçao maior(), que receba varios parametros com valores inteiros. seu programa tem que analisar os valores e dizer qual deles é o maior.
from random import randint
from time import sleep

def lin():
    print('=-'*30)

def maior(* num):
    lin()
    print('Analisando os valores passados...')
    for n in num:
        print(f'{n}', end=' ', flush=True)
        sleep(0.1)
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {max(num)}.')


maior(2, 9, 4, 5, 7, 1)
maior(4,7,0)
maior(1, 2)
maior(6)
maior(0)
lin()