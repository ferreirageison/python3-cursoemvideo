# calcular o seno, cosseno e a tangente de um valor em graus
from math import cos, tan, sin, radians
ang = float(input('Digite um ângulo: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print(f'O valor do seno de {ang}º é: {seno:.2f}º\n'
      f'O valor de cosseno de {ang}º é: {cosseno:.2f}º\n'
      f'O valor da tangente de {ang}º é: {tangente:.2f}º'
      )
