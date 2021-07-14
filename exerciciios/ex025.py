a1 = str(input('Digite o nome completo de uma pessoa : '))
a3 = a1.strip().lower().find('silva')
if a3 < 0:
    print('O nome {} nao possui a palavra Silva'.format(a1))
else:
    print('O nome {} possui a palavra Silva'.format(a1))
# ou
nom = str(input('digite o nome : ')).strip()
print('seu nome tem silva? {}'.format('silva' in nom.lower()))
