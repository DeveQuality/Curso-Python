""" CONDICOES ANINHADAS """

numero=int(input('teste sua saude com um numero de 1 a 13 :'))

saude = 10

if saude<numero: 
    print('estas saudavel e disposto , VAI A IGREJA !')
elif saude==numero:
    print('sua saude esta moderada, SE NAO ESTIVER SE SENTINDO BEM PODE DESCANSAR !')
else:
    print('sua saude esta baixa , VISITE UM MEDICO !')