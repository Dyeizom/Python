peso = float(input('Qual e o seu peso (KG): '))
altura = float(input('Qual e sua altura: '))

imc = peso / (altura * altura)

print(f'Seu IMC é {imc:.2f}')

if imc <= 18.5:
    print('Abaixo do Peso')
elif imc > 18.5 and imc < 25:
    print('Peso Ideal') 
elif imc >= 25 and imc >= 30:
    print('Sobrepeso')
elif imc > 30 and imc < 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade Morbida')