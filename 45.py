from datetime import date
data = date.today().year
contador = 0
contadorMA = 0
contadorME = 0


for x in range (0, 7):
     
    contador += 1
    ano = int(input(f'Digite {contador} o ano que você nasceu: '))
    idade = data - ano

    if idade >= 18:
        contadorMA += 1
    
    else: 
        contadorME += 1

    
print(f'Ao todo tivemos {contadorMA} pessoas maior de idade')
print(f'E tambem tivemos {contadorME} pessoas menores de idade')
