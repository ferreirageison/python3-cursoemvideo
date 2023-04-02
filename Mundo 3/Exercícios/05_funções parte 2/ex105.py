# crie um programa que tenha uma funçao chamada notas() que pode receber varias notas de alunos e vai retornar um dicionario com as seguintes infos: a) quant. de notas b) maior nota c) menor nota d) média da turma e) situacao(opcional). adicionar docstrings

def notas(*n, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.param n: uma ou mais notas dos alunos.
    param sit: mostra a situação com base na média (opcional).
    return: dicionário com várias infos sobre a situaçao da turma.'''
    from statistics import mean
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = mean(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

resp = notas(5.5, 9.5, 6.5, sit=True)
print(resp)