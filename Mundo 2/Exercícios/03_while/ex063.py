# escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci. ex: 0->1->1->2->3->5->8

n = int(input('Quantos valores da sequencia de fibonacci você deseja ver?: '))

# define os 2 primeiros termos da sequencia de fibonacci
a = 0
b = 1
print(f"{' La Sequenza Fibonacci ':=^60}")
print(f'{a} ... {b} ...', end=' ')

cont = 3
while cont <= n:
    c = a + b
    print(f'{c} ... ', end='')
    a = b
    b = c
    cont += 1
print('FIM')

# método com laço for
# for i in range(2, n): # incia do 2 por causa dos 2 primeiros termos já estarem definidos e printados na tela
#     c = a + b
#     print(f'{c} ... ' , end='')
#     a = b 
#     b = c 
# print('Fim')

