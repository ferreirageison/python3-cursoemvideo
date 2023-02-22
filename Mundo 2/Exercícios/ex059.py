# crie um programa que leia dois valores e mostre um menu na tela: [1]somar, [2]multiplicar, [3]maior, [4]novos números, [5]sair do programa. Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

option = 0

while option != 5:
    print(
        '''
            ===========> OPÇÕES <===========

            [1] + Somar
            [2] * Multiplicar
            [3] > Maior
            [4] Novos números
            [5] Sair do programa
            ''')
    option = int(input('Escolha uma opção: '))
    if option == 1:
        print(f'A soma entre os valores {n1} e {n2} é {n1 + n2}')
    elif option == 2:
        print(f'O produto entre os valores {n1} e {n2} é {n1 * n2}')
    elif option == 3:
        if n1 > n2:
            print(f'{n1} é o maior valor')
        elif n2 > n1:
            print(f'{n2} é o maior valor')
        else:
            print('Os valores são iguais.')
    elif option == 4:
        print('Digite os números novamente ')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif option == 5:
        print('Finalizando...')
    else:
        print('Opção inválida, digite novamente')