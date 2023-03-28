# faça um programa que leia o nome e média de um aluno, guardando também a situaçao em um dicionário. no final, mostre o conteúdo da estrutura na tela.

aluno = dict()

aluno['Nome'] = str(input('Nome: ')).strip().capitalize()
aluno['Media'] = float(input('Média: '))

if aluno['Media'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Media'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print('-='*30)
for k, v in aluno.items():
    print(f'    -{k} é igual a {v}')
