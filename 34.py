from random import choice
from time import sleep
usuario = str(input('Digite Pedra, Papel ou Tesoura: ')).upper().strip()

opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
maquina = choice(opcoes)

if usuario not in opcoes:
    print('Opção invalida, digite PEDRA, PAPEL OU TESOURA')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('POOO')
    sleep(1)
    print('VOCÊ: {} | MÁQUINA {}' .format(usuario, maquina))
    
    if usuario == maquina:
        print('EMPATE')
    elif usuario == 'PEDRA' and maquina == 'TESOURA' or \
         usuario == 'PAPEL' and maquina == 'PEDRA' or \
         usuario == 'TESOURA' and maquina == 'PAPEL':
         print('VOCÊ GANHOU! HAHAHAH')
    else:
        print('VOCÊ PERDEU!')
        