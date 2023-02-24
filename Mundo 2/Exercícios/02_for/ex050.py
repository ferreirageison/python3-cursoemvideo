# Ler 6 números inteiros e mostrar a soma dos pares. Desconsiderar o número ímpar digitado.
soma = 0
cont = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'A soma dos {cont} números pares digitados é {soma}')
