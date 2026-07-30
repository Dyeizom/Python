casa = float(input('Qual o valor da casa que o Sr. deja comprar R$ '))
salario = float(input('Qual e o valor do seu salario R$ '))
anos = float(input('Em quantos anos você pretende pagar este financeiamento: '))

x = anos * 12 # aqui multiplica a quantidade de anos por 12 = 72 meses.
valor = casa / x # aqui divide o valor da casa pela quantidade de meses mostrando o valor da parcela.

if valor >= (salario * 30/100 ):
    print('NEGADO! o valor da parcela ultrapassou 30% do sálario')
else:
    print('Aprovado! você paga {:g}x de R$ {:.3f} '.format(x, valor))

