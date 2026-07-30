soma = 0
contador = 0

for cn in range(1, 7):
    n = int(input(f'Digite o {cn} valor: '))
    if n % 2 == 0:
        soma += n
        contador += 1

print(f'Você digitou {contador} valores par \
e a soma dos valores pares é {soma}')