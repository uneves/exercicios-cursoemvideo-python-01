from datetime import date
ano = int(input('Digite o ano que quer analisar, digite zero para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é bissexto'.format(ano))
else:
    print('O ano de {} nao é bissexto'.format(ano))
