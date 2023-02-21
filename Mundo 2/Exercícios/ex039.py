from datetime import date
anoatual = date.today().year

gen = int(input('''Informe o gênero: 
[1] Masculino
[2] Feminino
[3] Outro 
'''))

if gen == 2 or gen == 3: # opção de escolha de alistamento
    opção = str(input('Você deseja se alistar no exército brasileiro? S/N ')).lower()
    if opção == 's':
        nasc = int(input('Digite o ano do seu nascimento: '))
        idade = anoatual - nasc
        if idade > 18:
            alist = anoatual - (idade - 18)
            print(
                f'Está atrasado {idade - 18} anos, filho!\n'
                f'Seu ano de alistamento foi em {alist}.') #pega a data anoatual subtrai o nascimento identificando a idade e subtrai 18 da idade para saber quantos anos de passaram desde os 18 anos
        elif idade == 18:
            print('É hora do filho chorar e da mãe não ver!')
        else:
            alist = anoatual + (18 - idade)
            print(
            f'Ainda faltam {18 - idade} anos para o inferno, filho!\n'
            f'Seu ano de alistamento é {alist}.')
    elif opção == 'n':
        print('Obrigado por sua participação.')
    else:
        print('Opção inválida.')
elif gen == 1:
    nasc = int(input('Digite o ano do seu nascimento: '))
    idade = anoatual - nasc
    if idade > 18:
        alist = anoatual - (idade - 18)
        print(
                f'Está atrasado {idade - 18} anos, filho!\n'
                f'Seu ano de alistamento foi em {alist}.') #pega a data anoatual subtrai o nascimento identificando a idade e subtrai 18 da idade para saber quantos anos de passaram desde os 18 anos
    elif idade == 18:
        print('É hora do filho chorar e da mãe não ver!')
    else:
        alist = anoatual + (18 - idade)
        print(
            f'Ainda faltam {18 - idade} anos para o inferno, filho!\n'
            f'Seu ano de alistamento é {alist}.')
else:
    print('Opção inválida.')