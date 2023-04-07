def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Falha na criação do arquivo.')
    else:
        print('Arquivo criado com sucesso.')


def lerArq(nome):
    from interface import cabeçalho
    try:
        a = open(nome, 'rt')
    except:
        print('Falha ao ler o arquivo.')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, n = 'Desconhecido', i = 'Desconhecido'):
    try:
        a = open(arq, 'at')
    except:
        print('Falha na abertura do arquivo.')
    else:
        try:
            a.write(f'{n}; {i}\n')
        except:
            print('Falha ao escrever os dados.')
        else:
            print(f'Novo registro de {n} adicionado.')
            a.close()