# soma entre os ímpares de 1 a 500 que são múltiplos de 3
soma = 0
cont = 0
for i in range (1, 501, 2):
    if i % 3 == 0: # pega os múltiplos de 3
        soma += i # soma todos os múltiplos de 3
        cont += 1 # conta quantos ímpares múltiplos de 3 tem entre 1 e 501
print(f'A soma de todos os {cont} valores ímpares múltiplos de 3 é {soma}')