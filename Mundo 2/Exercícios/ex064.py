# crie um programa que leia vários números inteiros por input. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag 999).

cont = 0
soma = 0
n = 0
while n != 999:
    n = int(input('Digite um valor: '))
    cont += 1
    soma += n
print(f'Foram digitados {cont} números e a soma entre todos eles é de {soma - 999}')