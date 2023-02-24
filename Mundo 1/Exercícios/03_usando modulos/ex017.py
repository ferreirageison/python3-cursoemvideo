from math import sqrt, pow
cop = float(input('Qual o valor do cateto oposto? '))
cad = float(input('Qual o valor do cateto adjacente? '))
h = sqrt(pow(cop,2) + pow(cad,2))
print(f'A hipotenusa deste triângulo-retângulo vale {h:.2f}')
