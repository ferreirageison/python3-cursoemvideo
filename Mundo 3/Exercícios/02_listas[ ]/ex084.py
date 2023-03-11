# faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. no final, mostre: a) quantas pessoas b) pessoas mais pesadas e seu peso c) pessoas mais leves e seu peso

# listas
pessoas = []
dados = []
resp = ''

# input
while 'n' not in resp:
    dados.append(str(input('Digite o nome: ')))
    dados.append(int(input('Digite o peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    resp = input('Deseja continuar? S/N: ').strip().lower()[0]

# listas e testes da mais pesada e mais leve
pesadas = pessoas[0]
leves = pessoas[0]
for p in pessoas:
    if p[1] > pesadas[1]:
        pesadas = p
    elif p[1] < leves[1]:
        leves = p

# output
    print('='*40)
    print(f'Total de pessoas: {len(pessoas)} ')
    print(f'A pessoa mais pesada é {pesadas[0].capitalize()} e pesa {pesadas[1]}')
    print(f'A pessoa mais leve é {leves[0].capitalize()} e pesa {leves[1]}')