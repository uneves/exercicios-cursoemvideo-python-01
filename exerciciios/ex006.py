n1 = float(input('\033[4;31mDigite um numero!\033[m '))
d1 = n1 * 2
t1 = n1 * 3
r1 = n1 ** (1/2)
print('O dobro de \033[4;32m{}\033[m é \033[4;33m{}\033[m, o triplo é \033[4;34m{:.2f}\033[m e sua raiz quadrada é '
      '\033[4;35m{:.2f}\033[m'.format(n1, d1, t1, r1))
# 'ou ainda usando uma variavel'
print('O dobro de {:.0f} é {:.0f}, \n''o triplo é {:.0f} \n''e sua raiz quadrada é {:.2f}'.format(n1, (n1 * 2), (n1 * 3), (n1 ** (1/2))))
# 'ou ainda usando uma variavel'
print('O dobro de {:.0f} é {:.0f}, \n''o triplo é {:.0f} \n''e sua raiz quadrada é {:.2f}'.format(n1, (n1 * 2), (n1 * 3), pow(n1, (1/2))))
