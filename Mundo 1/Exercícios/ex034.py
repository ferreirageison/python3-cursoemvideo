s = float(input('Digite o salário: '))
# if s >= 1250:
#     print(f'O salário teve um reajuste de 10% e agora é de R${s + (s * 10/100):.2f} reais')
# else:
#     print (f'O salário teve um reajuste de 15% e agora é de R${s + (s * 15/100):.2f} reais')
if s >= 1250:
    ns = s + (s * 10/100)
    print(f'O novo salário, com um reajuste de 10%, é de R${ns:.2f}')
else:
    ns = s + (s * 15/100)
    print(f'O novo salário, com um reajuste de 15%, é de R${ns:.2f}')
