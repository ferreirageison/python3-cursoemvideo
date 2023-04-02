# crie um programa que tenha uma funçao chamada fatorial() que receba 2 parametros: o 1 q indique o numero a calcular e o outro chamado show, q será um valor lógico(opcional) indicando se será mostrado ou nao na tela o processo de cálculo do fatorial.

def fatorial(n=1, show=0):
    '''
    -> calcula o fatorial de um número.
    param n: número a ser calculado.
    param show: mostra a conta completa e o fatorial (opcional).
    return: o valor do fatorial de um número n.'''

    print('-'*30)
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            if c > 1:
                print(f'{c}',  end=' x ')
            else:
                print(f'{c}', end=' = ')
    return f

# programa principal
print(fatorial(5, show=True))
# print(help(fatorial))