massa = float(input('Qual é o seu peso? '))
altura = float(input('Qual é sua altura? '))
imc = massa / altura ** 2
if imc <= 18.5:
    res = 'abaixo do peso'
elif imc <= 25:
    res = 'peso normal'
elif imc <= 30:
    res = 'acima do peso'
elif imc <=40:
    res = 'obeso'
else:
    res = 'obesidade mórbida'
print(f'Seu IMC é de {imc:.1f} e é considerado {res}.')
