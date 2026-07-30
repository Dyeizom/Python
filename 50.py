n = [7, 3, 12, 5, 9]

maior = n[0] # Inicializa com o primeiro elemento

for numero in n:
    if numero > maior:
        maior = numero
        print(f'{maior}')                                            