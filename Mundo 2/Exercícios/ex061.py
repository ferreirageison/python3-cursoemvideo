# refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura de teste lógico (while)

p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
d = p + (10 - 1) * r  # formula matemática para encontrar o termo
cont = 0
while cont != 10:
    for i in range(p, d + 1, r):
        cont += 1
        print(f'{cont:2}º termo: {i}')
print('Fim')
