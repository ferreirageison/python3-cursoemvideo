num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] Binário
[2] Octal
[3] Hexadecimal''')
choice = int(input('Sua opção: '))

#fórmulas de conversão com uso de funções específicas

if choice == 1:
    print(f'O valor {num} em binário é: {bin(num)[2:]}')
elif choice == 2:
    print(f'O valor {num} em octal é: {oct(num)[2:]}')
elif choice == 3:
    print(f'O valor {num} em hexadecimal é: {hex(num)[2:]}')
else:
    print('Opção inválida.')