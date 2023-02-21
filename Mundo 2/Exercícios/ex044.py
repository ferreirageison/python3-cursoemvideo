print(f'{" GF STORE ":=^50}')

preço = float(input('Qual o valor do(s) produto(s)? R$'))
pgto = int(input(
'''FORMAS DE PAGAMENTO
[1] Dinheiro ou PIX (10% de desconto)
[2] Débito à vista (5% de desconto)
[3] 2x no crédito
[4] 3x ou mais no crédito (20% de juros)
Selecione o modo de pagamento: '''))

# aumento ou desconto de acordo com o método de pagamento selecionado:
grana = preço - (preço * 10 / 100)
debito = preço - (preço * 5 / 100)
credito = preço + (preço * 20 / 100)

if pgto == 1:
    vf = grana
    print(f'O valor de R${preço:.2f} reais pago em dinheiro ou PIX recebe desconto e fica R${grana:.2f} reais')
elif pgto == 2:
    vf = debito
    print(f'O valor de R${preço:.2f} reais pago no débito à vista recebe desconto e fica R${debito:.2f} reais')
elif pgto == 3:
    print(f'O valor pago em 2x de R${preço / 2:.2f} reais no crédito vai custar um total de R${preço:.2f} reais')
elif pgto == 4:
    qparc = int(input('Quantas parcelas? '))
    if qparc <= 2:
        vparc = preço / qparc
        print(f'O valor a ser pago será de {qparc}x de {vparc:.2f} resultando no preço final de R${preço:.2f}')
    else:    
        vparc = credito / qparc
        print(f'O valor de R${preço:.2f} reais, parcelado em {qparc}x de R${vparc:.2f} no crédito, com acréscimo dos juros, resulta em um preço final de R${credito:.2f} reais')
else:
    print(f'{" ERRO ":#^50}')
    print('Opção inválida, escolha uma opção entre 1 e 4.')
