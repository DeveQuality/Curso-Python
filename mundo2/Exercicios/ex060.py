""" num=int(input('Digite um numero: '))

start=1
while num > 1:
    start=start*num
    num=num-1

print(start) """

""" from math import factorial

numero=int(input('Digite um numero para obter o fatorial: '))
f=factorial(numero)
print(' O fatorial do numero {} sera {}'.format(numero,f)) """

numero=int(input('Digite um numero para obter o fatorial: '))
c=numero
f=1
print('Calculando {}! = ' .format(numero),end='')
while c>0:
    print('{}'.format(c), end='')
    print(' x ' if c>1 else ' = ' , end='')

    f*=c
    c-=1
print('{}'.format(f))