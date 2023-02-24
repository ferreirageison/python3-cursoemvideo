preço = float(input('Informe o valor a ser financiado: R$'))
salário = float(input('Informe o salário do comprador: R$'))
anos = int(input('Informe a quantidade de anos: '))
prestação = preço / (anos * 12)
if prestação <= salário * 30/100:
    print(f'APROVADO. O valor da prestação será de R${prestação:.2f} reais')
else:
    print(f'NEGADO. O Salário é incompatível com a prestação de R${prestação:.2f} reais.')
