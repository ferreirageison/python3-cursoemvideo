# crie um programa que tenha uma funçao chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa, retornando um valor literal indicando se essa pessoa tem voto negado, opcionado ou obrigatório nas eleiçoes.

def voto(vetor):
    from datetime import date 
    idade = date.today().year - vetor
    if 65 > idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: NÃO VOTA.'

# programa principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))