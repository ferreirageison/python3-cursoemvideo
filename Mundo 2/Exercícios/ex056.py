# faça um programa que leia o nome, idade e sexo de 4 pessoas. No final ele deve mostrar: idade média do grupo, o nome do HOMEM mais velho e quantas mulheres têm menos de 20 anos.

idades = 0
menosvinte = 0
idadedovei = 0
nomedovei = ''
for i in range(1, 5):
    print(f'-----------{i}ª PESSOA-----------')
    nome = str(input('Nome: ')).strip().lower()
    idade = int(input('Idade: '))
    genero = str(input(('Sexo [H | M]: '))).strip().lower()
    idades += idade # soma as idades
    if genero == 'h' and i == 1:
        idadedovei = idade
        nomedovei = nome.capitalize()
    elif genero == 'h' and idade > idadedovei:
        nomedovei = nome.capitalize()
        idadedovei = idade
    if genero == 'm':
        if idade < 20:
            menosvinte += 1
media = idades / 4
print('-----------RESUMO-----------')
print(f''''O homem mais velho do grupo é {nomedovei} com {idadedovei} anos de idade\n
São {menosvinte} mulheres com menos de 20 anos\nA média total das idades do grupo é de
{media}''')