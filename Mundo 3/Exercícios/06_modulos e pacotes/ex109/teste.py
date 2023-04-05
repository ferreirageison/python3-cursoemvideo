# modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

# teste ex 109

from moeda import *

p = float(input('Digite o preço: R$'))
t = float(input('Digite a taxa: '))
print(f'A metade de {moeda(p)} é {metade(p, True)}')
print(f'O dobro de {moeda(p)} é {dobro(p, True)}')
print(f'Aumentando {t}%, temos {aumentar(p, t, True)}')
print(f'Diminuindo {t}%, temos {diminuir(p, t, True)}')

