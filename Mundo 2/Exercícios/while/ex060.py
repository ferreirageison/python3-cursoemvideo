# faça um programa que leia um número qualquer e mostre o seu fatorial usando for e while. ex: 5! = 5*4*3*2*1 = 120

n = int(input('Digite um número para calcular seu fatorial: '))

print(f'Calculando {n}! = ', end=' ')

# usando while
c = n
f = 1
# while c > 0:
#     print(f'{c}' , end=' ')
#     print('x' if c > 1 else '=', end=' ')
#     f *= c
#     c -= 1

# Usando for
for i in range(n, 0, -1):
    print(f'{i}', end=' ')
    print('x' if i > 1 else '=', end=' ')
    f *= i

print(f)
