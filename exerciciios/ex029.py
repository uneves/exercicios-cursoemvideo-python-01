vel1 = float(input('Digite a velocidade do veículo: '))
if vel1 <=80:
    print('Parabens, velocidade OK')
else:
    print('Voce foi multado em: R$ {:.2f}'.format((vel1-80)*7))
print('Tenha um bom dia dirija com seguranca')
##
# ou
##
vel1 = float(input('Digite a velocidade do veículo: '))
if vel1 > 80:
    print('Multado!voce excedeu o limite de velocidade que é de 80 Km/h')
    multa = (vel1 - 80) * 7
    print('Voce deve pagar uma multa de R$ {:.2f}'.format(multa))
print('Tenha um bom dia dirija com seguranca')
