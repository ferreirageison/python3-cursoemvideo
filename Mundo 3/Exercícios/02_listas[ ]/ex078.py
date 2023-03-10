# faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre o maior e o menor e suas posições na lista.

valores = []

for i in range(5):
    valores.append(int(input(f'Digite um valor para a posição {i}: ')))

maior = menor = valores[0] #insere o primeiro valor digitado nas variaveis maior e menor para comparar com os próximos valores digitados
pos_maior = [] # inicializam vazias para não gerarem resultados duplicados
pos_menor = []

# encontra e armazena nas listas vazias as posições do maior e menor mesmo repetidas
for i, valor in enumerate(valores):
    if valor > maior:
        maior = valor
        pos_maior = [i] # zera a lista e coloca o novo valor da posição do maior 
    elif valor == maior:
        pos_maior.append(i)
    if valor < menor: # outro if para que a iteração continue para o teste do menor
        menor = valor
        pos_menor = [i] # zera a lista e coloca o novo valor da posição do menor
    elif valor == menor: 
        pos_menor.append(i)

print(f'Você digitou os valores: {valores}')
print(f'O maior valor foi {maior} nas posições {pos_maior}')
print(f'O menor valor foi {menor} nas posições {pos_menor}')




