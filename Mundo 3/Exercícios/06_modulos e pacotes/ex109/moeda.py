# modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

# módulo ex 109

def dobro(preço, formato=False):
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço, formato=False):
    res = preço / 2
    return res if formato == False else moeda(res)


def aumentar(preço, taxa, formato=False):
    res = preço + (preço * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preço, taxa, formato=False):
    res = preço - (preço * taxa / 100)
    return res if formato == False else moeda(res)


def moeda(preço, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
