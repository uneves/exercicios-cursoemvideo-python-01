comp1 = float(input('Digite o comprimento da reta 01: '))
comp2 = float(input('Digite o comprimento da reta 02: '))
comp3 = float(input('Digite o comprimento da reta 03: '))
lista = (comp1, comp2, comp3)
lista2 = sorted(lista)
if lista2[2] ** 2 == (lista2[0] ** 2) + (lista2[1] **2):
    print('È possivel existir um triangulo com as medidas {}'.format(lista2))
else:
    print('Nao é possivel existir um triangulo com as medidas {}'.format(lista2))
