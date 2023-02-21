# ler peso de 5 pessoas e mostrar no final o maior e menor peso lidos

maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input(f'Peso da {i}ª pessoa: '))
    if i == 1: # primeira pessoa tem o maior e menor peso
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f'O maior peso é de {maior}\nO menor peso é de {menor}') 

# pesos = []
# for i in range(1,6):
#     peso = float(input(f'Digite o peso da {i}ª pessoa: '))
#     pesos += [peso]
# print(f'O maior peso lido foi de {max(pesos):.2f}\nO menor peso lido foi {min(pesos):.2f}')