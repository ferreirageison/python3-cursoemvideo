# crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

#módulo

def dobro(preço):
    return preço * 2

def metade(preço):
    return preço / 2

def aumentar(preço, taxa):
    return preço + (preço * taxa / 100)

def diminuir(preço, taxa):
    return preço - (preço * taxa / 100)
