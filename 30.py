from datetime import date

nascimento = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento
print('Sua idade é {} anos em {}'.format(idade, atual))
if idade == 18:
    print('Você precisa ir se alistar imediatamente'.format(idade))
elif idade < 18:
    saldo = 18 - idade
    print('Falta {} anos para você se alistar'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento sera em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você deveria ter se alistado a {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
