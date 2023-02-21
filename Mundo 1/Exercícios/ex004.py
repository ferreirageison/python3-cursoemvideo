# faça um programa que leia algo pelo teclado 
# e mostre na ela o seu tipo e todas as informações
# possíveis sobre ele (se é  número, alfabeto, espaço, capitulado, etc)

nl = input('Digite o que quiser: ')
print('O tipo primitivo de "{}" é {}:' .format(nl, type(nl)))
print('{} é um número:'.format(nl), nl.isnumeric())
print('{} é alfabetico:'.format(nl), nl.isalpha())
print('{} é um alfanumerico:'.format(nl), nl.isalnum())
print('{} é um espaço:'.format(nl), nl.isspace())
print('{} está em maiúsculas:'.format(nl), nl.isupper())
print('{} está em minúsculas:'.format(nl), nl.islower())
print('{} está capitalizado:'.format(nl), nl.istitle())
print('{} é um digito:'.format(nl), nl.isdigit())

#o "nl" é uma variável e objeto que tem caracteristicas e realiza
# funcionalidades com o uso de atributos e métodos()