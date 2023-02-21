# calculo de preço com 5%  desconto
preco = float(input('Qual o preço do produto? R$'))
novopreco = preco - (preco * 5/100)
print(f'O produto que custava R${preco:.2f} reais,'
f'agora na promoção, com com 5% de desconto, custa: R${novopreco:.2f} reais')
