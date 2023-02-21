A = float(input('Digite o comprimento de uma reta: '))
B = float(input('Digite outro comprimento de uma reta: '))
C = float(input('Digite mais um comprimento de uma reta: '))
if A + B > C and A + C > B and B + C > A:
    print('EUREKA! Podemos criar um triângulo.')
    if A == 3 and B == 4 and C == 5:
        print('Temos um triângulo pitagórico!')
else:
    print('Não é possível fazer um triângulo essas medidas.')
