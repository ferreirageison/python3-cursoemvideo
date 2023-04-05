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


def resumo(preço, taxaaum=10, taxared=5):
    print('-'*35)
    print(f'{"RESUMO DO VALOR":^35}')
    print('-'*35)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaaum}% de aumento: \t{aumentar(preço, taxaaum, True)}')
    print(f'{taxared}% de redução: \t{diminuir(preço, taxared, True)}')
    print('-'*35)