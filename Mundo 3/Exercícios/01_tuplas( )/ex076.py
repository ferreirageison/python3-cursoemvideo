# crie um programa que tenha uma tupla com nomes de produtos e seus respectivos preços. no final, mostre uma listagfem de preços, organizanddo os dados em forma tabular.

produtos = 'Café', 15, 'Feijão', 6, 'Arroz', 5, 'Macarrão', 3.5, 'Farinha', 9

for p in range(0, len(produtos)):
    if p % 2 == 0:
        print(f'{produtos[p]:.<20}', end='')
    else:
        print(f'R${produtos[p]:>7.2f}')