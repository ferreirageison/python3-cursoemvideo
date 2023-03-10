# crie um program que vai ler vários números e colocar em uma lista. depois mostrar: a) quantos números digitados. b) a lista de valores, ordenada de forma decrescente. c) se o valor 5 foi digitado e está ou não na lista.

valores = []
resp = ''
while True:
    valores.append(int(input('Digite um valor: ')))
    while 'sn' not in resp:
        resp = input('Quer continuar? S/N: ').lower().strip()[0]
        if resp in 'sn': 
            break
    if resp == 'n':
        break

print(f'Você digitou {len(valores)} elementos')
print(f'Os valores ordenados de forma decrescente são: {sorted(valores, reverse=True)}')
if 5 in valores:
    print(f'O valor 5 faz parte da lista e foi digitado na posição {valores.index(5)}!')
else:
    print('O valor 5 não faz parte da lista')