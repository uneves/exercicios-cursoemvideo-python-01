import math
num1 =int(input('Digite um numero: '))
num2 =int(input('Digite um segundo numero: '))
num3 =int(input('Digite um terceiro numero: '))
lista = (num1, num2, num3)
lista2 = (sorted(lista))
print('o maior valor é {} e o menor é {}'.format(lista2[-1], lista2[0]))
####
# ou
####
a = int(input('digite o primeiro valor: '))
b = int(input('digite o segundo valor: '))
c = int(input('digite o terceiro valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor valor digitado foi {}'.format(menor))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor digitado foi {}'.format(maior))
