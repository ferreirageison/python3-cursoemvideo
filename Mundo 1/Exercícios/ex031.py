d = float(input('Digite a distância da viagem: '))
# if d <= 200:
#     preço = d * 0.50
# else:
#     preço = d * 0.45
preço = d * 0.50 if d <=200 else d * 0.45 # operador ternário
print(f'O valor da passagem é R${preço:.2f} reais')
