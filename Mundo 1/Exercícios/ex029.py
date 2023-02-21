vel = float(input('Qual a velocidade do veículo em km/h: '))
multa = (vel - 80) * 7
if vel > 80:
    print('='*50)
    print(
        f'Acima do limite de velocidade de 80 km/h!\n'
        f'Valor da multa: R${multa:.2f} reais')
    print('-'*50)
else:
    print('='*50)
    print('Dentro do limite de velocidade, boa viagem!')
    print('-'*50)
print('Dirija com Segurança!')
print('='*50)