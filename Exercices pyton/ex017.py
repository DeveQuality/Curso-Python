import math
co = float(input('comprimento do cateto 0posto : '))
ca = float(input('comprimento do cateto adjacente'))

hi = math.hypot(co ,ca)

print('a hipotenusa vai medir{}'.format(hi))