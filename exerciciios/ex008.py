n1 = float(input('\033[1;31;43mDigite o valor em metros!\033[m '))
c1 = n1 * 100
m1 = n1 * 1000
print('O valor \033[4;35m{}\033[m em metros corresponde a \033[4;35m{}\033[m centimetros e a \033[4;35m{}\033[m milimetros'.format(n1, c1, m1))
# 'ou utilizando somente uma variavel'
print('O valor {:.1f} em metros corresponde a {:.0f} centimetros e a {:.0f} milimetros'.format(n1,n1 * 100, n1 * 1000))
