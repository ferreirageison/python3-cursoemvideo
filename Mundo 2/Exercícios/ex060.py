# faça um programa que leia um número qualquer e mostre o seu fatorial usando for e while. ex: 5! = 5*4*3*2*1 = 120

from math import factorial

n = int(input('Digite um número para calcular seu fatorial: '))

print(f'Calculando {n}! = ' , end=' ')

#usando while
# cont = n
# while cont > 0:
#     print(f'{cont}' , end=' ')
#     print('x' if cont > 1 else '=', end=' ')
#     cont -= 1

# Usando for    
for i in range(n, 0, -1):
    print(f'{i}' , end=' ')
    print('x' if i > 1 else '=' , end=' ')

print(factorial(n))

