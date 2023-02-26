# crie um programa que leia o nome e preço de vários produtos do carrinho de compras. o programa deverá perguntar se o usuário vai continuar. No final, mostre: a) qual o total de todos os produtos no carrinho. b) quantos prodsutos custam mais de R$1000. c) qual é o nome do produto mais barato.

print(f'{" CARRINHO DE COMPRAS ":#^40}')

itens = maisdemil = menorpreço = total = 0
barato = ' '
while True:
    produto = str(input('Digite o produto? ')).strip()
    preço = float(input('Qual o preço do produto R$'))
    itens += 1
    total += preço
    if preço > 1000:
        maisdemil += 1
    if itens == 1 or preço < menorpreço: # simplificado
        barato = produto
        menorpreço = preço
    # else:
    #     if preço < menorpreço:
    #         barato = produto
    #         menorpreço = preço
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Adicinar mais produtos? S/N: ')).lower().strip()  
    if continuar in 'n':
        break
print(f'''
Total de itens no carrinho: {itens}
Total da compra: R${total}
Quantos custam mais de R$1000: {maisdemil}
Produto mais barato: {barato} ''')
