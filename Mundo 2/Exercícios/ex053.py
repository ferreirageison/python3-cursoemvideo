# ler frase e informar se é um palíndromo desconsiderando os espaços
# exemplos: apos a soma; a sacada da casa; a torre da derrota; o lobo ama o bolo ; anotaram a data da maratona

frase = str(input('Digite uma frase: ')).strip().replace(' ', '').lower()
inverso = frase[::-1] #começa no início : até o fim : de trás pra frente -1

# comp = len(frase)
# inverso = ''
# while comp > 0:
#     inverso += frase[comp - 1]
#     comp -= 1 #índice de decremento

# for letra in range(comp -1, -1, -1):
# 	inverso += frase[letra]

if frase == inverso:
    print('Essa frase/palavra é um Palíndromo')
else:
    print('Essa é uma frase/palavra normal')
