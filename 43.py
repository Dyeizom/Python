from datetime import date

atual = date.today().year


n1 = int(input('Qual é a idade de nascimento: '))
#n2 = int(input('Qual é sua idade: '))


lista = [n1]
soma = sum(atual - lista)
print(soma)

'''maiorIdade = sum(1 for x in lista if x >= 21)
print(f'Tem {maiorIdade} maiores de idade')

menorIdade = sum(1 for x in lista if x < 21)
print(f'Tem {menorIdade} menores de idade')'''