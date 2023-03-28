# crie um programa que leia nome, sexo e idade de várias galera, guardando os dados de cada pessoa em um dict e todos os dicts em uma lista. no final, mostre: a) quantas pessoas foram cadastradas b) a média de idade do grupo c) uma lista com todas as mulheres d) uma lista com todas as pessoas com idade acimda da média

galera = []
pessoa = {}
acmedia = []
idades = 0
mulheres = []
repetir = sexo = ' '
while True:
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo: [M/F] '))
        if pessoa['Sexo'] in 'MmFf':
            break
        print('Erro! Por favor, digite apenas M ou F.')
    pessoa['Idade'] = int(input('Idade: '))
    idades += pessoa['Idade']
    galera.append(pessoa.copy())
    while True:
        repetir = str(input('Quer continuar? [S/N] '))
        if repetir in 'SsNn':
            break
        print('ERRO! Digite apenas S ou N.')

    if repetir in 'Nn':
        break

media = idades / len(galera)
for p in galera:
    if p['Idade'] > media:
        acmedia.append(p.copy())
for p in galera:
    if p['Sexo'] in 'Ff':
        mulheres.append(p['Nome'])

print('=-'*30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
print(f'B) A média de idades é de {media:.1f} anos.')
print(f'C) Mulheres cadastradas: {mulheres} ')
print(f'D) Lista das pessoas que estão acima da média:')
for p in acmedia:
    for k, v in p.items():
        print(f'    {k} = {v};', end='')
    print()
print('<< ENCERRADO >>')


