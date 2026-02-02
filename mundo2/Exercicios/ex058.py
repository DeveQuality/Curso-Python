import random
comp=random.randint(0,10)
tentantiva=0

usuario=int(input('Tente adivinhar o numero que o computador escolheu entre 0 a 10: '))

while comp != usuario:
   
    usuario=int(input('Voce perdeu ! Tente de novo: '))
    tentantiva+=1

print('Voce acertou  mas precisou de {} tentativa/s'.format(tentantiva))