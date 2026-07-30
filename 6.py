#CALCULO DE TINTA PARA PINTURA DE PAREDE
largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))

m2 = largura * altura
cobertura_por_litro = 2.0
tinta = m2 / cobertura_por_litro

print(f'Sua parede tem {largura:.2f} m de largura e {altura:.2f} m de altura, totalizando {m2:.3f} m². Você precisa de {tinta:.4f} litros de tinta.')