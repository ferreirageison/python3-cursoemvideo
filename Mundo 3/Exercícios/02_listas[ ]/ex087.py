# aprimore o desafio anterior, mostrando: a) valores pares b) a soma dos valores da coluna 3 c) o maior valor da segunda linha

# listas
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = soma3col = 0
# input
for l in range(3):
    for c in range(3):
        matrix[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

# pares
for l in matrix:
    for p, v in enumerate(l):
        if v % 2 == 0:
            somapares += v
    # soma terceira coluna
        if p == 2:
            soma3col += v

# output
for l in range(3):
    for c in range(3):
        print(f'[{matrix[l][c]:^5}]', end='')
    print()  # quebra a linha a cada laço completo de l e c
print('='*40)
print(f'A soma dos valores pares foi: {somapares}')
print(f'A soma dos valores da terceira coluna foi: {soma3col}')
print(f'O maior valor da segunda linha foi {max(matrix[1])}')
