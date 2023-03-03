# programa que leia 4 valores e guarde-os em uma tupla. no final, mostre: a) quantas vezes apareceu o 9. b) posição do 3. c)  os pares.

valores = (int(input('Digite o primeiro valor: ')),
           int(input('Digite o segundo valor: ')),
           int(input('Digite o terceiro valor: ')),
           int(input('Digite o quarto valor: ')))

print(f'Você digitou os valores {valores}')
print(f'O 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O 3 está na {valores.index(3) + 1}ª posição')
else:
    print('O 3 não apaeceu')
print('Números pares:', end=' ')
for n in valores:
    if n % 2 == 0:
        print(n, end=', ')
