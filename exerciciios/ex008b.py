n1 = float(input('\033[1;31;43mDigite uma distancia em metros!\033[m '))
print('\033[1;34m{:.1f}\033[m metros corresponden a :\n''\033[1;34m{:.3f}\033[m km\n''\033[1;34m{:.2f}\033[m hm\n''\033[1;34m{:.1f}\033[m dam'.format(n1, n1 / 1000, n1 / 100, n1 / 10))
print('\033[1;34m{:.0f}\033[m dm\n''\033[1;34m{:.0f}\033[m cm\n''\033[1;34m{:.0f}\033[m mm'.format(n1 * 10, n1 * 100, n1 * 1000))
