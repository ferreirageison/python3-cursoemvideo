# adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

# teste ex 108

import moeda

p = float(input('Digite o preço: R$'))
t = float(input('Digite a taxa: '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando {t}%, temos {moeda.moeda(moeda.aumentar(p, t))}')
print(f'Diminuido {t}%, temos {moeda.moeda(moeda.diminuir(p, t))}')