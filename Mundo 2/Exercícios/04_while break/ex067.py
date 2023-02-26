# faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

# c = t = 0
# n = int(input('Digite um número para ver sua tabuada: '))
# while True:
#     c += 1
#     t = n * c
#     print(f'{n} X {c} = {t}')
#     if c == 10:
#         n = int(input('Digite um número para ver sua tabuada: '))
#         c = 0
#         if n < 0:
#             break
# print('FIM')

# resolução do professor Guanabara
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} X {c} = {n * c}')
print('FIM')
