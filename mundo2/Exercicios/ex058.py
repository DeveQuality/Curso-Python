""" import random
comp=random.randint(0,10)
tentantiva=0

usuario=int(input('Tente adivinhar o numero que o computador escolheu entre 0 a 10: '))

while comp != usuario:
   
    usuario=int(input('Voce perdeu ! Tente de novo: '))
    tentantiva+=1

print('Voce acertou  mas precisou de {} tentativa/s'.format(tentantiva)) """

from random import randint
computador=randint(0,10)
print('Sou o seu  computador... acabei de pensar em um numero entre 0 a 10.')
print('Sera que consegue adivinhar qual foi? ')

acertou=False
tentativas=0

while not acertou:
    jogador=int(input('Qual o seu palpite? '))
    tentativas+=1
    if jogador == computador:
        acertou=True
    else:
        if jogador < computador:
            print('\033[33m tente um valor maior!')
        elif jogador > computador:
            print('\033[34m tente um valor menor! ')
print('Parabens! voce acertou com {} tentativas!'.format(tentativas))