import random
lista = (0, 1, 2, 3, 4, 5)
num1 = random.choice(lista)
#print(num1)
print('Pensei em um numero, tente adivinhar...')
num2 = int(input('Digite um numero de 1 a 5: '))
print('voce acertou o numero escolido!' if num1==num2 else 'voce errou o numero é {}'.format(num1))
print('Parabens!!!'if num1==num2 else'Tente outro vez!')
#---------
# ---ou---
#---------
from random import randint
from time import sleep
computador = randint(0, 5) # busca um numero aleatório no intervalo
print('-=-'*20)
print('Vou pensar em um numero entre 0 e 5 tente advinhar: ')
print('-=-'*20)
jogador =int(input('Digite um numero de 1 a 5: ')) # jogador tenta advinhar
print('Processando...')
sleep(3)
if jogador == computador:
    print('Parabéns voce conseguiu me vencer!')
else:
    print('Ganhei! eu pensei no número {} e nao no {}'.format(computador, jogador))
