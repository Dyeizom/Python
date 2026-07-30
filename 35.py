num = int(input('Digite um numero inteiro: '))
print('''Escolha uma base para conversão
      [1] BINÁRIO
      [2] OCTAL
      [3] HEXADECIMAL ''')
opção = int(input('Digite uma opção: '))

if opção == 1:
    print('A CONVERSÃO PARA BINÁRIO É {} '.format(bin(num)[2:]))
elif opção == 2:
    print('A CONVERSSÃO PARA OCTAL É {} '.format(oct(num)[2:]))
elif opção == 3:
    print('A CONVERSÃO PARA HEXADECIMAL É {} '.format(hex(num)[2:]))
elif opção != 1 or 2 or 3:
    print('OPÇÃO INVALIDA DIGITE 1, 2 OU 3')