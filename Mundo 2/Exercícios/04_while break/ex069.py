# crie um programa que leia a idade de várias pessoas. a cada pessoa cadastrada, o programa devrá perguntar se o usuário quer continuar. No final, mostre: a) quantas pessoas tem + de 18. b) quantos homens foram cadastrados. c) quantas mulheres tem menos de 20 anos.

print('----------------------')
print('CADASTRO DE CLIENTES')
print('----------------------')

maiores = homens = menos20 = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('Digite o sexo [ M | F ]: ')).strip().lower()[0]
    print('----------------------')
    if idade >= 18:
        maiores += 1
    if sexo == 'm':
        homens += 1
    elif sexo == 'f' and idade < 20:
        menos20 += 1
    sair = ' '
    while sair not in 'sn':
        sair = str(input('Continuar? [S | N]: ')).strip().lower()[0]
    print('----------------------')
    if sair == 'n':
        break
print(f'''Total de homens: {homens}
Total de maiores de 18: {maiores}
Total de mulheres menores de 20: {menos20}  
''')


    



