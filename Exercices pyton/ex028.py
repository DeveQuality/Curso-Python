import random

computador= random.randint(0,5)     
"""faz o computador pensar em um numero de 0 a 5"""

usuario=int(input('adivinhe o numero  do computador de 0 a 5 : '))

print('Digitaste o numero {} '.format(usuario) )

print('O numero do computador foi {}'.format(computador))

if computador != usuario:
    print('Opha vc perdeu ! tenta de novo.')
else:
    print('Aweee! Ganhaste bay! Quer jogar de novo ?')
