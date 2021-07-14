n1 = float(input('\033[4;34;43mDigite um número inteiro!\033[m '))
s1 = n1 + 1
a1 = n1 - 1
print('O sucessosr de {} é {} eo antecessor é {}{}{}'.format(n1, s1, '\033[1;34m', a1, '\033[m'))
# 'ou usando uma variavel)'
print('O sucessosr de {} é {} eo antecessor é {}{}{}'.format(n1, n1+1, '\033[1;33m', n1 - 1, '\033[m'))
# 'ou ainda usando uma variavel)'
print('O sucessosr de {:.0f} é {:.0f} eo antecessor é {}{:.0f}{}'.format(n1, (n1+1), '\033[1;32m', (n1 - 1), '\033[m'))
