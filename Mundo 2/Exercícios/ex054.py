#ler o ano de nascimento de 7 pessoas, no final mostrar quantas atingiram a maioridade (21 anos) e quantas não
from datetime import date
atual = date.today().year
maior = 0
menor = 0
for i in range(1, 8):
    nasc = int(input('Em que ano a pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'São {maior} pessoas maiores de idade e {menor} pessoas menores de idade')
