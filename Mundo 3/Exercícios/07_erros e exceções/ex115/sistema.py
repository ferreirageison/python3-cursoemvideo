# crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples. o sistema só vai ter 2 opçoes: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

from interface import *
from arquivo import *
from time import sleep

#testa se o arquivo já existe e cria se ainda não
arq = 'cursoemvideo.txt'
if not arqExiste(arq):
    criarArq(arq)

while True:
    resp = menu(['Listar pessoas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resp == 1:
        lerArq(arq)
    elif resp == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        sleep(1)
        break
    else:
        print('\033[0;31mERRO: por favor, digite uma opção válida.\033[m')
        sleep(1)
        continue
