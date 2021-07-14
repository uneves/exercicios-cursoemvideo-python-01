#import math
from math import sqrt
catop = float(input('medida do cateto oposto'))
cataj = float(input('medida do cateto adjacente'))
hipot = sqrt(catop**2 + cataj**2)
# ou hipot = (catop**2 + cataj**2)**1/2
print('No triangulo onde o cateto op {} e adjacente {} \n''a hipotenusa é {:.2f}'.format(catop, cataj, hipot) )
#ou usando a funcao hypot
from math import hypot
catop = float(input('medida do cateto oposto'))
cataj = float(input('medida do cateto adjacente'))
hipot = hypot(catop, cataj)
print('No triangulo onde o cateto op {} e adjacente {} \n''a hipotenusa é {:.2f}'.format(catop, cataj, hipot) )



