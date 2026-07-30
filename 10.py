aluguel = float(input('Quantos dias alugado ? '))
km = float(input('Quantos Km rodados ? '))

v1 = aluguel * 60
v2 = km * 0.15
valor = v1 + v2

print('Valor R$ {:.2f} '.format(valor))