# ler quanto dinheiro uma pessoa tem e mostrar cotação em dolar
r = float(input('Quanto dinheiro você tem em reais? R$'))
c = r / 3.27
print('Com R${:.2f} reais você pode comprar o equivalente a U${:.2f} dólares!'.format(r, c)) 