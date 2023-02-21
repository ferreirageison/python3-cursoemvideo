nome = str(input('Digite seu nome o completo: ')).strip()
#nome2 = len(nome.replace(' ', '')) substitui os espaços vazios por nenhum espaço
# nome2 = len(nome) - nome.count(' ') # pega a quantidade de caracteres e subtrai pelo total de espaços vazios
print(f'Em maiúsculas: {nome.upper()}')
print(f'Em minúsculas: {nome.lower()}')
print(f'O seu nome completo tem {len(nome.replace(" ", ""))} letras')
# print(f'O seu primeiro nome tem {nome.find(" ")} letras')
print(f'O seu primeiro nome é {nome.split()[0]} e ele tem {len(nome.split()[0])} letras')