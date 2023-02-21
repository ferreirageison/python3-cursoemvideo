nome = str(input('Digite seu nome completo: ')).strip()
# if 'silva' in nome.lower():
#     print('Você é um Silva')
# else:
#     print('Você não é um Silva')
print(f'Seu nome tem Silva? {"silva" in nome.lower()}')