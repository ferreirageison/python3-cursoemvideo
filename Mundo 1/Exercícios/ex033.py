n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite o último número: '))
# num = [n1, n2, n3]
# if n1 == n2 and n1 == n3:
#     print('Os números são todos iguais')
# else:
#     print(
#         f'O maior número é {max(num)}\n'
#         f'O menor número é {min(num)}'
#         )
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
if n1 == n2 and n3:
    print('Tudo igual')
else:
    print(
            f'O maior valor digitado foi {maior}\n'
            f'O menor valor digitado foi {menor}'
            )
