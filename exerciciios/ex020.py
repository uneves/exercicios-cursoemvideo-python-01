from random import shuffle
a1 = str(input('Escreva o nome do primeiro aluno :'))
a2 = str(input('Escreva o nome do segundo aluno :'))
a3 = str(input('Escreva o nome do terceiro aluno :'))
a4 = str(input('Escreva o nome do quarto aluno :'))
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentecao é {}'.format(lista))
# ou
import random
a1 = str(input('Escreva o nome do primeiro aluno :'))
a2 = str(input('Escreva o nome do segundo aluno :'))
a3 = str(input('Escreva o nome do terceiro aluno :'))
a4 = str(input('Escreva o nome do quarto aluno :'))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentecao é {}'.format(lista))


