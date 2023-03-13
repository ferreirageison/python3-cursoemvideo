# crie um programa onde o usuário digite 7 valores numéricos, e cadastre-os separados em lista dentro de uma única lista. no final mostrar valores pares e ímpares em ordem crescente.

#lista única
valores = [[], []]

#input  e teste 
for i in range(1, 8):
    num = int(input(f'Digite o {i}º valor: '))
    if num not in valores[0]:
        if num % 2 == 0:
            valores[0].append(num)
        elif num not in valores[1]:
            valores[1].append(num)
#output
print(f'Os valores pares digitados foram: {sorted(valores[0])}')
print(f'Os valores ímpares digitados foram: {sorted(valores[1])}')

