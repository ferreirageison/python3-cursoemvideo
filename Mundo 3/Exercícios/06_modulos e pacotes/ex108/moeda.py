# adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

#módulo ex 108

def dobro(preço):
    return  preço * 2

def metade(preço):
    return  preço / 2

def aumentar(preço, taxa):
    return preço + (preço * taxa / 100)

def diminuir(preço, taxa):
    return  preço - (preço * taxa / 100)

def moeda(preço, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')