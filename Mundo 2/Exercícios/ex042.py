# refazer exercício 35 informando cada tipo de triângulo formado.
a = float(input('Digite um comprimento de reta: '))
b = float(input('Digite outro comprimento de reta: '))
c = float(input('Digite outro comprimento de reta: '))
print('Analisando seguimentos...')
if a + b > c and b + c > a and c + a > b:
    print('Os seguimentos informados formam um Triângulo ' , end='')
    if a == b == c:
        print('EQUILÁTERO')
    elif a != b != c != a:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Triângulo impossível')
