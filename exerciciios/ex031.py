dist = float(input('Informe a distancia da viagem: '))
if dist<=200:
    print('O valor da viagem é: R$ {:.2f}'.format(dist*0.5))
else:
    print('O valor da viagem é: R$ {:.2f}'.format(dist*0.45))
####
# ou
####
dist = float(input('Informe a distancia da viagem: '))
print('voce está prestes a comecar uma viagen de {} km'.format(dist))
if dist<=200:
    preco = dist * 0.50
else:
    preco = dist * 0.45
print('E o preco de sua passagem será de R$ {:.2f}'.format(preco))
#####
# ou
#####
dist = float(input('Informe a distancia da viagem: '))
print('voce está prestes a comecar uma viagen de {} km'.format(dist))
preco = dist * 0.50 if dist <= 200 else dist * 0.45
print('E o preco de sua passagem será de R$ {:.2f}'.format(preco))
