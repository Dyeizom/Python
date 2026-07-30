n1 = float(input('Qual foi a primeira nota: '))
n2 = float(input('Qual foi a segunda nota: '))

media = (n1 + n2)  / 2

if media < 5.0:
    print('REPROVADO, SUA MEDIA FOI {} '.format(media))
elif media <= 5.0 and media <= 6.9:
    print('RECUPERAÇÃO, SUA MÉDIA FOI {} '.format(media))
elif media >= 7.0:
    print('APROVADO, SUA MÉDIA FOI {} '.format(media))