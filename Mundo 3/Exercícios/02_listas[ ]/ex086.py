# crie um programa que crie uma matriz de dimensao 3x3 e preencha com valores lidos pelo teclado. no final mostre a matriz na tela, com a formatação correta.

#listas
matrix = []
dado = []

#input
for i in range(3):
    dado.append(int(input(f'Digite um valor para {i}/0: ')))
    dado.append(int(input(f'Digite um valor para {i}/1: ')))
    dado.append(int(input(f'Digite um valor para {i}/2: ')))
    matrix.append(dado[:])
    dado.clear()

#output
print(matrix[0])
print(matrix[1])
print(matrix[2])