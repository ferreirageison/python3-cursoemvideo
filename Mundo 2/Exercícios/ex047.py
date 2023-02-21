# crie um programa que mostra na tela 
# todos os números pares que estão entre
# 1 e 50

for i in range(1, 51):
    print('.', end='')# cada ponto mostra um laço completo 
    if i % 2 == 0:
        print(i, end=' ')
print('Fim')
