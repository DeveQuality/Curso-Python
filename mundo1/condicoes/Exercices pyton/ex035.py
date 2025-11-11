r1=float(input("Digite o valor do primeiro ângulo: "))
r2=float(input("Digite o valor do segundo ângulo: "))
r3=float(input("Digite o valor do terceiro ângulo: "))

print('---RESULTADO-------------------------------------------------------------------------')

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('estes segmentos podem formar um triângulo')
else:
    print('estes segmentos não podem formar um triângulo')
