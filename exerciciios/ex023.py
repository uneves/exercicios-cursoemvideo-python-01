#a1 = str(input('Digite um numero de 1 a 9999 :'))
#a2 = a1[0]
#a3 = a1[1]
#a4 = a1[2]
#a5 = a1[3]
#print('Para o numero {} temos:\n Unidade : {}\n Dezena : {}\n Centena : {}\n Milhar : {} '.format(a1, a5, a4, a3, a2))
# acima nao funciona com numeros com menos de 4 digitos abaixo a solucao correta
num = int(input('digite um numero :'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('analisando o numero {}'.format(num))
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))
