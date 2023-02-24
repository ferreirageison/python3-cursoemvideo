# crie um programa que leia vários números inteiros por input. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag 999).

# cont = 0
# soma = 0
# n = 0

n = cont = soma = 0 # se todos recebem o mesmo valor, a sintaxe pode ser facilitada
n = int(input('Digite um valor [999 para parar]: '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um valor [999 para parar]: '))
print(f'Foram digitados {cont} números e a soma entre todos eles é de {soma}')