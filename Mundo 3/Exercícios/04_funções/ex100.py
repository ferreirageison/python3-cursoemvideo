# faça um programa que tenha uma lista chamada números e duas funçoes chamadas sorteia() e somaPar(). a primeira funçao vai sortear 5 números e colocá-los dentro da lista e a segunda vai mostrar a soma entre todos os pares sorteados pela funcao anterior.
from random import randint
from time import sleep

def lin():
    print('=-'*30)

def sorteia(vetor):
    lin()
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(5):
        n = randint(1, 9)
        vetor.append(n)
        print(f'{n}, ', end='', flush=True)
        sleep(0.5)
    print('FIM!')

def somaPar(vetor):
    lin()
    somap = 0
    for n in vetor:
        if n % 2 == 0:
            somap += n
    print(f'Somando os valores pares de {vetor}, temos {somap}')
    lin()


numeros = []
sorteia(numeros)
somaPar(numeros)