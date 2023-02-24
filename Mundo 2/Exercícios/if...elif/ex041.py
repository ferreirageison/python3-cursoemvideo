from datetime import date
ano = int(input('Qual o ano de nascimento do atleta: '))
idade = date.today().year - ano
if idade <= 9:
    cat = 'MIRIM'
elif idade <= 14:
    cat = 'INFANTIL'
elif idade <= 19:
    cat = 'JUNIOR'
elif idade == 20:
    cat = 'SÊNIOR'
else:
    cat = 'MASTER'
print(f'O atleta tem {idade} anos e está na cat {cat}')
