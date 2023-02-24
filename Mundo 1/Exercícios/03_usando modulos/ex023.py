num = int(input('Digite um número: '))
u = num // 1 % 10 #pega o resultado da divisão inteira e o resultado do módulo (resto)  
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000
print(
    f'Analisando o número {num}\n'
    f'Unidade: {u}\n'
    f'Dezena: {d}\n'
    f'Centena: {c}\n'
    f'Milhar: {m}\n'
)
