# crie um programa que leia vários números inteiros por input. no final, que ele mostre a média entre todos os valores e qual foi o maior e o menor. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resp = 's'
soma = 0
cont = 0

while resp == 's':
    cont += 1
    n = int(input('Digite um número: '))
    soma += n
    resp = str(input('Quer digitar outro? S|N: ')).strip().lower()
    media = soma / cont
print('========================================')
print(f'Soma dos valores digitados: {soma}')
print(f'Quantidade de valores digitados: {cont}')
print(f'Média entre os valores digitados: {media:.0f}')
print('========================================')
    
