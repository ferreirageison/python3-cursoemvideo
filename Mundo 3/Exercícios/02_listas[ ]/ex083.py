# crie um programa onde o usuário digite uma expressão qualquer que use parênteses. seu aplicativo deverá analisar se a expressão passada está com os parêntes abertos e fechados na ordem correta.

# Contador de parênteses
# contador = 0

# expressao = input('Digite uma expressão: ')

# # Percorrer cada caractere da expressão
# for v in expressao:
#   # Se for um parêntese aberto, aumentar o contador
#   if v == "(":
#     contador += 1
#   # Se for um parêntese fechado, diminuir o contador
#   elif v == ")":
#     contador -= 1
#   # Se o contador ficar negativo, a expressão é inválida
#   if contador < 0:
#     break

# # Se o contador for zero no final, a expressão é válida
# if contador == 0:
#   print("Expressão Válida")
# else:
#   print("Expressão Inválida")

pilha = []
expressao = input('Digite uma expressão: ')
for v in expressao:
    if v == '(':
        pilha.append(v)  # adiciona um '(' aberto na pilha
    elif v == ')':
        if len(pilha) > 0:  # testa se a já pilha foi preenchida 
            pilha.pop()  # se tiver, remove '(' da pilha
if len(pilha) == 0:  # se nenhum parenteses aberto sobrando na pilha
    print('Expressão válida')
else:
    print('Expressão inválida')
