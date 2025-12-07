pt=int(input('digite o primeiro termo: '))
r=int(input('digite a razao: '))

decimo=pt+(10-1)*r

for b in range(pt , decimo ,r):
    print(b, end='… ')

print('Acabou!') 



""" decimo termo significa os dez numeros pulando da razao ou
    ele pula do valor da razao ate chegar dez vezes
"""