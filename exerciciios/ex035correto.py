a = float(input('Digite o lado 01: '))
b = float(input('Digite o lado 02: '))
c = float(input('Digite o lado 03: '))
if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print('O triangulo de lados {}, {} e {} pode existir'.format(a, b, c))
else:
    print('O triangulo de lados {}, {} e {} nao pode existir'.format(a, b, c))
######
# ou
######
print('-='*20)
print('Analisador de triangulos')
print('-='*20)
r1 = float(input('Digite o lado 01: '))
r2 = float(input('Digite o lado 02: '))
r3 = float(input('Digite o lado 03: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('o tirangulo de lado {}, {} e {} é possivel'.format(r1, r2, r3))
else:
    print('o tirangulo de lado {}, {} e {} nao é possivel'.format(r1, r2, r3))
