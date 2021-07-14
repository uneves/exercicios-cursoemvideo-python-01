a1 = str(input('Digite o nome de uma cidade : '))
a3 = a1.strip().lower().find('santo')
if a3 != 0:
       print('O nome da cidade {} nao comeca pela palavra Santo'.format(a1))
else:
       print('O nome da cidade {} comeca pela palavra Santo'.format(a1))
# ou
cid = str(input('em que cidade voce nasceu? ')).strip()
print('o seu nome possui a palavra Santo: {}'.format(cid[0:5].upper() == 'SANTO'))
