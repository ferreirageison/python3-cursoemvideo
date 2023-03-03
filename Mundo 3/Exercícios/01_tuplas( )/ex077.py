# crie um programa que tenha uma tupla com várias palavras (sem acento). mostrar para cada palavra quais são as suas vogais.

# cria uma tupla com 10 palavras (sem acento)
palavras = ("casa", "mesa", "cadeira", "livro", "caneta", "janela", "porta", "flor", "arvore", "carro")

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos: ', end='')
    for letra in palavra:
        if letra in 'aeiou':
          print(letra.upper(), end=', ')