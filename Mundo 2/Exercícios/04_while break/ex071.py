# crie um simulador de caixa eletrônico que pergunte o valor a ser sacado. o programa responde quantas cedulas de cada valor serao entregues. usar cedulas de 50, 20, 10 e 1.  

# => minha resolução

# saldo = um = dez = vinte = cinquenta = 0
# print(f'{" CAIXA ELETRÔNICO LA CASA DI PAPEL " :-^50}')
# saque = int(input('Qual valor quer sacar? R$'))
# print('------------------------------------')
# while saque > 1:
#     if saque >= 50:
#         cinquenta = saque // 50
#         saldo = 50 * cinquenta
#         saque -= saldo
#     if saque >= 20 and saque < 50:
#         vinte = saque // 20
#         saldo = 20 * vinte
#         saque -= saldo
#     if saque >= 10 and saque < 20:
#         dez = saque // 10
#         saldo = 10 * dez
#         saque -= saldo
#     if saque > 1 and saque < 10:
#         um = saque // 1
#         saldo = 1 * um
#         saque -= saldo
# print(f'''Efetuando seu saque em...

# {cinquenta} notas de R$50,00
# {vinte} notas de R$20,00
# {dez} notas de R$10,00
# {um} notas de R$01,00
# ------------------------------------
# Obrigado, volte sempre!
# ''')

# => resolução do professor Guanabara

# valor = int(input('Que valor você quer sacar? R$'))
# total = valor
# nota = 50
# totalnotas = 0
# while True:
#     if total >= nota:
#         total -= nota
#         totalnotas += 1
#     else:
#         if totalnotas > 0:
#             print(f'Total de {totalnotas} cédulas de R${nota}')
#         if nota == 50:
#             nota = 20
#         elif nota == 20:
#             nota = 10
#         elif nota == 10:
#             nota = 1
#         totalnotas = 0
#         if total == 0:
#             break

# => Melhor solução encontrada no comentário do video da aula no youtube
valorSaque = int(input('Valor do saque: R$ '))
print('-' * 40)
for nota in [50, 20, 10, 1]:
    quantidade = valorSaque // nota # encontra a quantidade de notas
    valorSaque = valorSaque % nota # atualiza oq falta sacar p/ próxima nota do loop
    if quantidade > 0:
        print(f'{quantidade} notas de R$ {nota}')

