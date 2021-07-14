#import math
from math import trunc
num = float(input('Escreva um número real com 3 ou mais casas decimais'))
print('O número real {} equivale ao numero inteiro {:.0f}'.format(num, trunc(num)))
# ou truncando na formatacao do campo
num = float(input('digite um valor'))
print('A porcao inteira de {} é {:.0f}'.format(num, num))
# ou usando a funcao int no .format
num = float(input('digite um valor'))
print('A porcao inteira de {} é {}'.format(num, int(num)))

