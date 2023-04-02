# crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda
# from moeda import metade, dobro, aumentar, diminuir
# from moeda import *

p = float(input('Digite o preço: R$'))
t = float(input('Digite a taxa: '))
print(f'A metade de R${p} é R${moeda.metade(p)}')
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
print(f'Aumentando {t}%, temos R${moeda.aumentar(p, t)}')
print(f'Diminuido {t}%, temos R${moeda.diminuir(p, t)}')