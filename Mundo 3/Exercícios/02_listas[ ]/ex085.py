# crie um programa onde o usuário digite 7 valores numéricos, e cadastre-os separados em lista dentro de uma única lista. no final mostrar valores pares e ímpares em ordem crescente.

#listas
valores = []
pares = []
ímpares = []

#input 
for i in range(7):
    valores.append(int(input('Digite um valor: ')))

#teste par ou impar
for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        ímpares.append(v)

#output
print(f'Os valores pares digitados foram: {sorted(pares)}')
print(f'Os valores ímpares digitados foram: {sorted(ímpares)}')

