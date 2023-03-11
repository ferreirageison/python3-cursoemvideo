# aprimore o desafio anterior, mostrando: a) valores pares b) a soma dos valores da coluna 3 c) o maior valor da segunda linha

#listas
matrix = []
dado = []
somapares = soma3col = maior2l = 0
 
#input
for i in range(3):
    dado.append(int(input(f'Digite um valor para {i}/0: ')))
    dado.append(int(input(f'Digite um valor para {i}/1: ')))
    dado.append(int(input(f'Digite um valor para {i}/2: ')))
    matrix.append(dado[:])
    dado.clear()

#pares
for l in matrix:
    for p, v in enumerate(l):
        if v % 2 == 0:
            somapares += v
        elif v % 2 == 0:
            somapares += v
        elif v % 2 == 0:
            somapares += v
    #soma terceira coluna
        if p == 2:
            soma3col += v

#output
print(matrix[0])
print(matrix[1])
print(matrix[2])
print('='*40)
print(f'A soma dos valores pares foi: {somapares}')
print(f'A soma dos valores da terceira coluna foi: {soma3col}')
print(f'O maior valor da segunda linha foi {max(matrix[1])}')