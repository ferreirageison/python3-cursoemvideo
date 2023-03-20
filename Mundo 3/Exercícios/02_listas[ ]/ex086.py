# crie um programa que crie uma matriz de dimensao 3x3 e preencha com valores lidos pelo teclado. no final mostre a matriz na tela, com a formatação correta.

# listas
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# input
for l in range(3):
    for c in range(3):
        matrix[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

# output
for l in range(3):
    for c in range(3):
        print(f'[{matrix[l][c]:^5}]', end='')
    print() #quebra a linha a cada laço completo de l e c