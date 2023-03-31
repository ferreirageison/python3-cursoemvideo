# faça um programa que tenha uma funçao chamada area(), que receba as dimensoes de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(l, c):
    mq = l * c
    print('-'*20)
    print(f'A área de um terreno com {larg}m de largura e {comp}m de comprimento é de {mq}m²')

larg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))

area(larg, comp)