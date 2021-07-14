n1 = float(input('\033[1;34;43mDigite o valor em Reais a ser convertido em Dolares!\033[m R$ '))
n2 = float(input('\033[1;33;44mQuantos reais um dolar vale hoje?\033[m '))
r1 = n1 / n2
print('O valor de \033[1;34m{}\033[m Reais corresponde a R$ \033[1;34m{:.2f}\033[m Dolares'.format(n1, r1))
