import math
# ou  from math import sin, tan, cos, radians
angulo1 = float(input('escreva o valor do angulo'))
angulo = math.radians(angulo1)
seno = sin(angulo)
coseno = cos(angulo)
tangente = tan(angulo)
print('a partir de {} graus temos: \n''seno de {:.3f} ,\n''coseno de {:.3f} e\n''tangente de {:.3f}'.format(angulo1, seno, coseno,tangente))
