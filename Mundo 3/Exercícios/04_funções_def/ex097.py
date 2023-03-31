# faça um programa que tenha uma funçao chamada escreva(), que receba um texto qualquer como parametro e mostre uma mensagem com tamanho adaptavel.

def escreva(txt):
    t = len(txt) + 4
    print(f'~'*t)
    print(f'  {txt}')
    print(f'~'*t)


escreva('Hello, World!')
escreva('Curso de Python no Youtube')
escreva('CeV')