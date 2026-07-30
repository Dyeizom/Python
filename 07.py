preço = float(input('Qual o preço do produto R$ '))

desc = preço - (preço * 5 / 100)

print('O valor real deste produto é R$ {:.2f} e com o desconto de 5% ele fica R$ {:.2f}' .format(preço, desc))
