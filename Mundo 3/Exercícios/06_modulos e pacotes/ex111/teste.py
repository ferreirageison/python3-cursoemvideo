# teste ex 111

from utilidadesCeV import moeda, dado


# p = float(input('Digite o preço: R$'))
p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 35, 22)