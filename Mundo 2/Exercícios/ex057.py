# faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'H'ou 'M'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = ''
sexo = str(input('Qual o seu sexo? [H | M] ')).strip().lower()
while sexo != 'h' and sexo != 'm':
    sexo = str(input('Essa opção não é válida. Escolha entre estas duas opções: [H | M]: '))
if sexo == 'm':    
    print(f'Voce digitou {sexo.upper()} de Mulher.')
else:
    print(f'você digitou {sexo.upper()} de Homem')