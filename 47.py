
pessoa = 0
somaI = 0
mediaI = 0
idadeHMV = 0
maisvelhoH = ''
idadeM20 = 0
for pessoa in range(1, 5):

    print(f'{pessoa}ª PESSOA')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('M/F: ')).upper()
    somaI += idade
    if sexo == 'M' and idade > idadeHMV:
       idadeHMV = idade
       maisvelhoH = nome
    if sexo == 'F' and idade < 20:
        idadeM20 += 1
mediaI = somaI / 4
print(f'A media de idade do grupo é de {mediaI} anos')
print(f'O homen mais velho tem {idadeHMV} e se chama {maisvelhoH}')
print(f'Total de {idadeM20} abaixo dos 20 anos')