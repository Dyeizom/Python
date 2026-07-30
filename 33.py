produto = float(input('Qual o valor do produto R$ '))
fpagamento = str(input('''Qual a forma de pagamento ?
[1] AVISTA - DINHEIRO OU CHEQUE
[2] AVISTA NO CARTÃO
[3] 2X NO CARTÃO
[4] 3X OU MAIS NO CARTÃO  
                       ''')).lower()

desc10 = produto -  (produto * 10/100)
desc5 = produto - (produto * 5/100)
card2x = produto
card3x = produto + (produto * 20/100)


if fpagamento == '1':
    print('Sua compra fica no valor de R$ {:.2f} '.format(desc10))
elif fpagamento == '2':
    print('Sua compra fica no valor de R$ {:.2f} '.format(desc5))
elif fpagamento == '3':
    print('Sua compra fica no valor de R$ {:.2f} '.format(card2x))
elif fpagamento == '4':
    Xparcelas = int(input('Qual a quantidade de parcelas: '))
    Tparcelas = card3x / Xparcelas
    print('Sua compra fica no valor de R$ {:.2f} dividido em {}x de {:.2f} COM JUROS'.format(card3x, Xparcelas, Tparcelas))