'''import math
num = float(input('type a number :'))

porcaointeira = math.trunc(num)

print(' a porcao inteira do valor {} é {}'.format(num,porcaointeira))'''

from math import trunc

num = float(input('type a number : '))
print('o valor digitado foi {} e a porcao inteira é de {}'.format(num,trunc(num)))