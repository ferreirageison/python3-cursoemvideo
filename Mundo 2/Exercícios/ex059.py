# crie um programa que leia dois valores e mostre um menu na tela: [1]somar, [2]multiplicar, [3]maior, [4]novos números, [5]sair do programa. Seu programa deverá realizar a operação solicitada em cada caso.

option = 0
while option != 5:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
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
        print(f'A soma dos valores é {n1 + n2}')
    if option == 2:
        print(f'O produto dos valores é {n1 * n2}')
    if option == 3:
        if n1 > n2:
            print(f'O {n1} é o maior valor')
        elif n2 > n1:
            print(f'O {n2} é o maior valor')
        else:
            print('Os valores são iguais.')
