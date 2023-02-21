nome = input('Digite seu nome completo: ').strip()
nome = nome.split()
print(
    f'Primeiro nome: {nome[0]}\n'
    f'Último nome: {nome[-1]}' # -1 sempre retorna o último item da lista
)