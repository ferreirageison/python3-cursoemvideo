# reescreva a funcao leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade de digitacao de um numero de tipo inválido. aproveite e crie tambem uma funcao leiaFloat().

def leiaInt(x):
    while True:
        try:
            n = int(input(x))
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não digitar nada.\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        else:
            return n
        

def leiaFloat(x):
    valido = True
    while valido:
        try:
            n = float(input(x))
            valido = False
        except KeyboardInterrupt:
            valido = False
            print('\033[0;31mO usuário preferiu não digitar nada.\033[m')
            return 0
        except:
            print('\033[0;31mERRO: por favor, digite um número real válido.\033[m') 
        else:
            return n         


inteiro = leiaInt('Digite um valor inteiro: ')
real = leiaFloat('Digite um valor real: ')

print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')
