import random
a1 = str(input('Escreva o nome do primeiro aluno :'))
a2 = str(input('Escreva o nome do segundo aluno :'))
a3 = str(input('Escreva o nome do terceiro aluno :'))
a4 = str(input('Escreva o nome do quarto aluno :'))
lista = [a1, a2, a3, a4]
a5 = random.choice(lista)
print('Entre os alunos:\n{}\n{}\n{}\n{}\no escolhido é {}'.format(a1, a2, a3, a4, a5))
