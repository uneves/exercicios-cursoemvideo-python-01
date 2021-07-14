a1 = str(input('digite o nome completo :'))
a2 = a1.title().split()
print('Para o nome {}\n primeiro = {}\n último = {}'.format(a1.title(), a2[0], a2[-1]))
# ou
print('Para o nome {}\n primeiro = {}\n último = {}'.format(a1.title(), a2[0], a2[len(a2)-1]))
