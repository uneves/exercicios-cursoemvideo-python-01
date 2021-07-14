sal = float(input('Digite o Salário do funcionário: '))
if sal <= 1250:
    print('O salario de R$ {:.2f} com aumento será de R$ {:.2f}'.format(sal, (sal + (sal * 15 / 100))))
else:
    print('O salario de R$ {:.2f} com aumento será de R$ {:.2f}'.format(sal, (sal + (sal * 10 / 100))))
######
#ou
######
sal = float(input('Digite o salário do funcionário: '))
if sal <= 1250:
    novo = sal + (sal * 15 / 100)
else:
    novo = sal + (sal * 10 / 100)
print('Para quem ganhava R$ {:.2f} o novo salário é de {:.2f}'.format(sal, novo))
