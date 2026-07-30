soma = 0
cont = 0
for numero in range(1, 501):
    if numero % 2 != 0 and numero % 3 == 0:
        cont += 1
        soma += numero

print(f"A soma de todos os valores {cont} é: {soma}")