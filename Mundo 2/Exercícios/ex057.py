# faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'H'ou 'M'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = ''
sexo = str(input('Qual o seu sexo? [H | M] ')).strip().lower()[0] # [0] pega o primeiro caractere da string
# while sexo != 'h' and sexo != 'm':
while sexo not in 'HhMm': #uso de 'not in' diminui e simplifica o código    
    sexo = str(input('Essa opção não é válida. Escolha entre as duas opções disponíveis: [H | M]: ')).strip().lower()[0]
if sexo == 'm':    
    print(f'Voce digitou {sexo.upper()} de Mulher.')
else:
    print(f'você digitou {sexo.upper()} de Homem')