'''import math

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjecente: '))

hi = math.hypot(co, ca)

print('A hipotenusa vai medir {:.2f}' .format(hi))'''

from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjecente: '))

hi = hypot(co, ca)

print('A hipotenusa vai medir {:.2f}' .format(hi))