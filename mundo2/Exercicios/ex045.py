""" import random

jogo=int(input('Quer Jogar comigo? Escolha : 0-Pedra  1-Papel  2-Tesoura :  '))

lista=['pedra','papel','tesoura']

escolha=random.randint(0,2)

if lista[jogo == escolha]:
    print('{} .Empate'.format(escolha))
elif lista[escolha==1]:
    print('{} .Empate'.format(escolha))

print(escolha) """

import random

escolha=random.randint(1,3)

pedra=1
papel=2
tessoura=3


print(papel)
print(escolha)