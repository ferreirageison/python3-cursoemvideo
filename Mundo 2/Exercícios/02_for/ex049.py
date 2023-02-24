# refazer o ex09.py usando o for
n = int(input('Digite um número para ver sua tabuada: '))
print(f'Com vocês a tabuada do {n}')
for i in range(1, 11):
    print(f'{n} x {i} = {n * i}')
