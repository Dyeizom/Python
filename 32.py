from datetime import date

atual = date.today().year

ano = int(input('EM QUE ANO VOCÊ NASCEU: '))

idade = atual - ano

if idade <= 9:
    print('{} ANOS, VOCÊ ESTA NA CATEGORIA MIRIM '.format(idade))
elif idade <= 14:
    print('{} ANOS, VOCÊ ESTA NA CATEGORIA INFANTIL '.format(idade))
elif idade <= 19:
    print('{} ANOS, VOCÊ ESTA NA CATEGORIA JUNIOR '.format(idade))
elif idade <= 20:
    print('{} ANOS, VOCE ESTA NA CATEGORIA SENIOR '.format(idade))
elif idade >= 21:
    print('{} ANOS, VOCE ESTA NA CATEGORIA MASTER ' .format(idade))