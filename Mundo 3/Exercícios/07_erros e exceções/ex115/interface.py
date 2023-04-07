def linha(tam = 42):
    print('-' * tam)

def cabeçalho(txt):
    linha()
    print(txt.center(42))
    linha()


def menu(lista):
    from time import sleep
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for i in lista:
        print(f'{c} - {i}')
        c += 1
    linha()
    while True:
        try:
            opc = int(input('Digite uma opção: '))
        except:
            print('\033[0;31mERRO: por favor, digite uma opção válida.\033[m')
            sleep(1)
            continue
        else:
            return opc