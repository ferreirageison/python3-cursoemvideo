# crie um programa que leia vários números inteiros por input. no final, que ele mostre a média entre todos os valores e qual foi o maior e o menor. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
r = 's'
s = q = m = 0 #soma, quantidade e média
while r in 'Ss':
    n = int(input('Digite um número: '))
    s += n # soma
    q += 1 # quantidade de números digitados
    r = str(input('Quer continuar? S|N: ' )).strip()[0]
    if q == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
m = s / q # média
print(f'Você digitou {q} números e a média entre eles foi {m}')
print(f'O maior valor digitado foi {maior} e o menor {menor}')