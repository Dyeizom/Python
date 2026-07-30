'''n = int(input('Escolha uma tabuada ? '))
print('{} x {:2} = {}' .format(1, n, n*1))
print('{} x {:2} = {}' .format(2, n, n*2))
print('{} x {:2} = {}' .format(3, n, n*3))
print('{} x {:2} = {}' .format(4, n, n*4))
print('{} x {:2} = {}' .format(5, n, n*5))
print('{} x {:2} = {}' .format(6, n, n*6))
print('{} x {:2} = {}' .format(7, n, n*7))
print('{} x {:2} = {}' .format(8, n, n*8))
print('{} x {:2} = {}' .format(9, n, n*9))
print('{} x {} = {}' .format(10, n, n*10))'''

tabuada = int(input('ESCOLHA A TABUADA: '))

for i in range(1, 11):
    print(f'{i} x {tabuada} = {tabuada*i}')