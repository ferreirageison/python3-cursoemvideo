# crie um programa que leia nome, ano de nasc e carteira de trab e cadastre-os(com idade) em um dicionário. se a carteira for != de 0, o dicionário receberá também o ano de contrataçao e o salário. calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar (considerar 35 anos de contribuiçao).
from datetime import date
year = date.today().year

cadastro = {}

cadastro['Nome'] = input(str('Nome: ')).strip().capitalize()
nasc = int(input('Ano de nascimento: '))
cadastro['Idade'] = year - nasc
cadastro['CTPS'] = int(input('Carteira de trabalho (0 se não tem): '))
if cadastro['CTPS'] != 0:
    cadastro['Salário'] = float(input('Salário R$')) 
    contratacao = int(input('Ano de Contratação: '))
    cadastro['Idade aposentadoria'] = cadastro['Idade'] + (contratacao + 35) - year
    
print('=-'*30)
for k, v in cadastro.items():
    print(f'    -{k} tem o valor {v}')