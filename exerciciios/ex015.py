da = int(input('Quantidade de dias alugados! '))
km = float(input('Quantidade de Km rodados! '))
vt = (da * 60) + (km * 0.15)
print('O total a pagar é de R$ {:.2f}'.format(vt))
