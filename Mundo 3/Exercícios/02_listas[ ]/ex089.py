# crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta. no final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente. 

# #listas
# alunos = []
# notas = []
# medias = []
# dados = []
# maisum = 's'
# notasind = 0

# #input
# while maisum not in 'n':
#     dados.append(str(input('Digite o nome do aluno: ')).strip().capitalize())
#     dados.append(float(input('Digite sua primeira nota: ')))
#     dados.append(float(input('Digite sua segunda nota: ')))
#     alunos.append(dados[:])
#     dados.clear()
#     maisum = str(input('Inserir mais um S/N?: ')).lower().strip()[0]
#     if maisum == 'n':
#         break
# #notas
# for i in range(len(alunos)):
#     notas.append(alunos[i][1:3])
# #medias
# for n in notas:
#     medias.append((n[0] + n[1]) / 2)

# print('=-'*40)
# print(f'{"Nº NOME"}', end='')
# print(f'{"MEDIA":>30}')
# print('-'*40)
# for i in range(len(alunos)):
#     print(f'{i}', end='  ') #index
#     print(f'{alunos[i][0]:<30}', end='') #nome
#     print(f'{medias[i]:>4.1f}') #media

# while True:
#     notasind = int(input('Deseja mostrar as notas de qual aluno? (999 para sair): '))
#     if notasind == 999:
#         print('Finalizando... Volte sempre!')
#         break
#     print('-'*40)
#     print(f'As notas da {alunos[notasind][0].capitalize()} foram {notas[notasind]}')
#     print('-'*40)
    
#resolucao do professor

ficha = list()
while True:
    nome = str(input('Nome: ')).strip().capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'nN':
        break

print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{media:>8.1f}')
while True:
    resp2 = int(input('Deseja ver as notas de qual aluno? (999 para sair) '))
    if resp2 == 999:
        print('Finalizando... Volte sempre!')
        break
    else:
        print(f'As notas do aluno {ficha[resp2][0]} foram: {ficha[resp2][1]}')