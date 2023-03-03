# crie um programa que gere cinco números aleatórios em uma tupla. Depois, mostre a listagem de números gerados e indique o menor e o maior que estão na tupla.

from random import randint

numeros = randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9)
# numeros = tuple(randint(i, 9) for i in range(0, 5)) # soluçao com tuple

maior = max(numeros)
menor = min(numeros)
print(
    f'''Os valores sorteados foram: {numeros}
O maior número é: {maior}
O menor número é: {menor}'''
)