'''import math
angulo = float(input('Digite o angulo que você deseja: '))

se = math.sin(math.radians(angulo))
co = math.cos(math.radians(angulo)) 
ta = math.tan(math.radians(angulo))

print('O Ângulo de {:.2f} tem o SENO de {:.2f} '.format(angulo, se))
print('O Ângulo de {:.2f} tem o COSSENO {:.2f} ' .format(angulo, co))
print('O Ângulo de {:.2f} tem o TANGENTE {:.2f} ' .format(angulo, ta))'''

from math import radians, sin, cos, tan

angulo = float(input('Digite o angulo que você dejsa: '))

se = sin(radians(angulo))
co = cos(radians(angulo))
ta = tan(radians(angulo))

print('O angulo de {:.2f} tem o SENO de {:.2f}' .format(angulo, se))
print('O angulo de {:.2f} tem o COSSENO {:.2f}' .format(angulo, se))
print('O angulo de{:.2f} tem o TANGENTE {:.2f}' .format(angulo, ta))
