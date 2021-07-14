n1 = float(input('\033[1;31mDigite a primeira nota do aluno!\033[m '))
n2 = float(input('\033[1;32mDigite a segunda nota do aluno!\033[m '))
m1 = (n1+n2)/2
print('A média da primeira nota \033[4;34m{}\033[m e da segunda nota \033[4;34m{}\033[m, \né igual a \033[4;34m{:.1f}\033[m '.format(n1, n2, m1))
# 'ou usando menos a variavel m1'
print('A média da primeira nota {:.1f} e da segunda nota {:.1f}, \n''é igual a {:.1f} '.format(n1, n2,(n1 + n2) / 2))
