# melhore o desafio anterior (061), perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
d = p + (10 - 1) * r  # fórmula matemática para encontrar o 10º termo em uma P.A.
cont = 0
resp = 's'
while resp == 's':
    for i in range(p, d + 1, r):
        cont += 1
        print(f'{cont:2}º termo: {i}')
    resp = str(input('Quer ver os próximos 10 termos? S | N: ')).lower().strip()
    if resp == 's':
        p = d + r # atualiza o primeiro termo 'p' com o que seria próximo (11º) da sequencia anterior, usando a razão
        d = p + (10 - 1) * r # atualiza a formula a partir do primeiro termo atualizado
print('Fim')