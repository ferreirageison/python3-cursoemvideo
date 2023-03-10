# crie um programa que leia vários números em uma lista. depois crie duas listas extras que vão conter apenas o valores pares e os valores ímpares digitados, respectivamente. ao final, mostre o conteúdo das 3 listas.

valores = []
pares = []
ímpares = []

resp = ''
while True:
    valores.append(int(input('Digite um valor: ')))
    while 'sn' not in resp:
        resp = input('Quer continuar? ').lower().strip()[0]
        if resp in 'sn':
            break
    if resp == 'n':
        break
for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        ímpares.append(v)

print('='*40)
print(f'Lista completa: {valores}')
print(f'Lista somente com os pares: {pares}')
print(f'Lista somente com os ímpares: {ímpares}')
print('='*40)