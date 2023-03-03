# crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extensão, de zero até vinte. seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = 0
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        print(f'Você digitou {extenso[n]}')
        p = input('Quer continuar? S/N: ').lower()[0]
        if p == 'n':
            break
    else:
        print('Tente novamente')
        
    