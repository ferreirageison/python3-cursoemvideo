# faça um mini sistema que utilize o interactive help do python. o usuário vai digitar o comando e o manual vai aparecer. quando o usuário digitar a palavra 'fim', o programa se encerrará. obs. usar cores.

cores = {
    'sem cor': '\033[m',
    'vermelho': '\033[0;30;41m',
    'verde': '\033[0;30;42m',
    'amarelo': '\033[0;30;43m',
    'azul': '\033[0;30;44m',
    'roxo': '\033[0;30;45m',
    'branco': '\033[7;30m'
}


def ttl(txt, cor):
    msg = txt
    comp = len(msg) + 4
    print(cores[cor], end='')
    print('~' * comp)
    print(f'  {msg}')
    print('~' * comp)
    print(cores['sem cor'], end='')


def ajuda(cmdlet):
    from time import sleep
    ttl(f"Acessando o manual do comando '{cmdlet}'", 'azul')
    print(cores['roxo'], end='')
    help(cmdlet)
    print(cores['sem cor'], end='')
    sleep(0.5)


# programa principal
ttl('SISTEMA DE AJUDA PyHELP', 'verde')
while True:
    c = input('Função ou biblioteca > ')
    if c == 'fim':
        ttl('ATÉ LOGO', 'vermelho')
        break
    ajuda(c)
