# crie um programa que tenha uma funçao chamada leiaInt(), q vai funcionar de forma semelhante a funcao input() do python, só q fazendo a validacao para aceitar apenas um valor numérico. ex: n = leiaint('Digite um numero: ')

def leiaInt(x):
    n = input(x)
    if n.isnumeric():
        return n
    else:
        print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        return leiaInt(x)

#programa principal
n = leiaInt('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {n}')