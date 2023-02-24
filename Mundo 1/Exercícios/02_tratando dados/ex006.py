# crie um algoritmo que leia um numero e mostre o seu dobro, o triplo e raiz quadrada
n = int(input('Digite um valor: '))
nd = n * 2
nt = n * 3
nz = n ** (1/2)
print('O dobro de {} vale {}\nO triplo de {} vale {}\nA raiz quadrada de {} vale {:.1f}'.format(
    n, nd, n, nt, n, nz))
