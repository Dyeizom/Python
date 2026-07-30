contador = 0
maior = 0 
menor = 0

for contador in range(1, 6):
    peso = float(input(f'Peso da {contador}ª pessoa: '))
    if contador == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
            
        if peso < menor:
            menor = peso
    
print(f'O maior peso digitado foi de {maior}kg')
print(f'O menor peso digitado foi de {menor}kg')