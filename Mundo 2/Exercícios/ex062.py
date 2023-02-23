# melhore o desafio anterior (061), perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

t = p
c = 0
l = 10

# versão onde pergunta se s ou n para mostrar os próximos 10 termos
# user = 's'
# while user == 's': 
#     print(f'{t}',  end=' ')
#     print('->', end=' ')
#     t += r
#     c += 1
#     if c == l:
#         print('PAUSA')
#         user = str(input('\nDeseja ver os próximos 10 termos? S|N: '))
#         l += 10
# print('Fim')

# versão onde pergunta a quantidade de termos para mostrar na sequencia 
user = 1
while user != 0: 
    print(f'{t}',  end=' ')
    print('->', end=' ')
    t += r
    c += 1
    if c == l:
        print('PAUSA')
        user = int(input('\nQuantos mais deseja ver na sequencia? : '))
        l += user
print('Fim')