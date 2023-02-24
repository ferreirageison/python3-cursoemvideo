# ler número inteiro e dizer se é um número primo

n = int(input('Digite um numero: '))
totdiv = 0  # variável mais importante pois vai guardar a quantidade de vezes que um número é divisível
print('São divisores: ', end='')
for i in range(1, int(n/2)+1): # pega do 1 até metade do número lido, porque nenhum número é divisível por mais da metade dele mesmo
    if n % i == 0:  # verifica se é divisível pelas voltas do laço
        totdiv += 1  # soma a quantidade de vezes que o n é divisível
        print(i,  end=', ') # números divisíveis
if totdiv == 1:  # se um número for divisível apenas uma vez até a sua metade, ou seja, por 1, então ele é primo, senão não é primo
    print(f'\n{n} é um número primo')
else:
    print(f'\n{n} não é um número primo')
