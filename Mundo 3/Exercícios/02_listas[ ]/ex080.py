# crie um programa que leia 5 valores numéricos em uma lista, já na posição correta de inserção, sem uso da função sorted().
valores = []
for i in range(5):
    valor = int(input('Digite um valor: '))
    for p in range(len(valores)): 
        if valor < valores[p]: # testa se o valor digitado é menor que o valor na posição p da lista valores, que está vazia da primeira vez 
            valores.insert(p, valor) # insere o menor valor na posição p, deslocando o valor atual para frente
            print(f'Valor {valor} adicionado na posição {p}...')
            break
    else: # se não encontrou nenhum valor menor na estrutura for, então adiciona o valor ao final da lista
        valores.append(valor)
        print('Valor adicionado ao final da lista...')  
print(valores)