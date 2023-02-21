# escreva um programa que mostre na tela
# uma contagem regressiva para o estouro
# de fogos de artifício, indo de 10 até 0
# com uma pausa de 1 segundo entre eles
# dica: função sleep()
from time import sleep
for i in range(10, -1, -1):
    print(f'{i}...')
    sleep(0.5)
print('Feliz ano novo!')
