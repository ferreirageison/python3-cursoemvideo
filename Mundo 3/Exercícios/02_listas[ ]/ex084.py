# faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. no final, mostre: a) quantas pessoas b) pessoas mais pesadas e seu peso c) pessoas mais leves e seu peso

# listas
pessoas = []
dados = []
resp = ''

# input de nome e peso
while 'n' not in resp:
    dados.append(str(input('Digite o nome: ')).capitalize())
    dados.append(float(input('Digite o peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    resp = input('Continuar? S/N: ').lower().strip()[0]

# variaveis e listas de peso
maior = menor = pessoas[0][1]
nomemaior = [] 
nomemenor = []

# laço p encontrar os pesos 
for p in pessoas:
    if p[1] > maior:
        maior = p[1]
        nomemaior.clear()
        nomemaior = [p[0]]
    elif p[1] == maior:
        nomemaior.append(p[0])
    if p[1] < menor:
        menor = p[1]
        nomemenor.clear()
        nomemenor = [p[0]]
    elif p[1] == menor:
        nomemenor.append(p[0])

# output
print('='*40)
print(f'Total de pessoas: {len(pessoas)} ')
print(f'A(s) pessoa(s) mais pesada(s): {nomemaior} com o peso de {maior}kgs')
print(f'A(s) pessoa(s) mais leve(s): {nomemenor} com o peso de {menor}kgs')