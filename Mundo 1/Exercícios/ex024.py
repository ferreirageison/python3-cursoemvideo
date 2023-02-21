# o programa deve dizer se existe SANTO no primeiro nome
cidade = str(input('Digite o nome da sua cidade: ')).strip()
if cidade.lower()[:5] == 'santo':
    print('Essa cidade começa com Santo')
else:
    print('Essa cidade não começa com Santo')