# refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura de teste lógico (while)

p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

#t = 1 
# while t <= 10:
#     d = p + (t - 1) * r # formula matemática para encontrar o termo
#     print(f'{t}º termo: {d}')
#     t += 1
# print('Fim')

t = p
c = 1
while c <=10:
    print(f'{t} -> ', end='')
    t += r
    c += 1
print('Fim')