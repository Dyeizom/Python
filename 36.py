l1 = int(input('PRIMEIRO SEGMENTO: '))
l2 = int(input('SEGUNDO SEGMENTO '))
l3 = int(input('TERCEIRO SEGMENTO '))

'''Os triângulos são classificados quanto aos lados em três tipos: 
equilátero (três lados iguais), isósceles (dois lados iguais) e escaleno (três lados diferentes). '''


if l1 == l2 == l3:
    print(f'OS TRÊS SEGMENTOS {l1}, {l2}, {l3} COM OS TRÊS VALORES IGUAIS FORMA UM EQUILATERO')
elif l1 == l2 or l2 == l3 or l1 == l3:
    print(f'OS TRÊS SEGMENTOS {l1}, {l2}, {l3} COM DOIS VALORES IGUAIS FORMA UM ISOSCELES')
elif l1 != l2 or l2 != l3 or l1 != l3:
    print(f'OS TRÊS SEGMENTOS {l1}, {l2}, {l3} COM OS TRÊS VALORES DIFERENTES FORMA UM ESCALENO')