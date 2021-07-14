n1 = float(input('Digite o valor do produto! R$ '))
d1 = (n1 * 5) / 100
n2 = n1 - d1
print('O produto custa R$ {:.2f}, seu desconto de 5% é de R$ {:.2f}\n'' e o valor final é R$ {:.2f}'.format(n1, d1, n2))
