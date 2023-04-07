# crie um código que teste se o site pudim.com.br ou qualquer outro está acessível ou nao.

import urllib.request

try:
    site = urllib.request.urlopen('https://google.com.br')
except urllib.error.URLError:
    print('deu ruim')
else:
    print('deu bom')
    print(site.read())