a1 = str(input('digite uma frase :'))
a2 = a1.strip().lower().find('a')
a3 = a1.strip().lower().rfind('a')
if a2 >= 0:
 print('Na frase {}\na letra "a" aparece primeiro na posicao {} e por ultimo na posicao {}'.format(a1, a2, a3))
else: print('Na frase {} a letra a nao aparece em nenhuma posicao '.format(a1))
print('A letra a aparece  {} vezes'.format(a1.strip().lower().count('a')))
#ou
frase = str(input(' digite uma frase: '))
print('a letra A aparece {} vezes'.format(frase.strip().upper().count('A')))
print('a letra A aparece primeiro na posicao {}'.format(frase.strip().upper().find('A')+1))
print('a letra A aparece por último na posicao {}'.format(frase.strip().upper().rfind('A')+1))
