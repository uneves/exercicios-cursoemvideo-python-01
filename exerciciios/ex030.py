import math
num = int(input('Digite um numero inteiro: '))
#print(math.remainder(num, 2))
if math.remainder(num, 2)==0:
    print('O número {} é par'.format(num))
else:
    print('O número {} é impar'.format(num))
####
# OU
####
num = int(input('Digite um numero inteiro: '))
resultado = num % 2 # % informa o resto da divisao
if math.remainder(num, 2)==0:
    print('O número {} é par'.format(num))
else:
    print('O número {} é impar'.format(num))