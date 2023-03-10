# crie um programa que cadastre vários valores numéricose cadastre-os em uma lista. caso o número já exista, ele não deve ser adicionado. no final, serão exibidos todos os valores únicos digitados em ordem crescente.

# valores = []
# while True:
#     valor = int(input('Digite um valor: '))
#     valores.append(valor)
#     if valores.count(valor) > 1:
#         valores.remove(valor)
#         print('Valor duplicado e descartado')
#     check = ' '
#     while check not in 'sn':
#         check = input('Quer continuar? S/N: ').lower().strip()[0]
#     if check == 'n':
#         break
# print(sorted(valores))

valores = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado')
    else:
        print('Valor duplicado descartado')
    check = ' '
    while check not in 'sn':
        check = input('Quer continuar? S/N: ').lower().strip()[0]
    if check == 'n':
        break
print(sorted(valores))