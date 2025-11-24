s=0

for b in range(0 ,6):
    nr=int(input('digite um numero: '))
    
    if nr%2==0:
        s+= nr  
        print('Numero par')
    else:
        print('Numero impar')
        
print('a soma dos valores pares sera de {}'.format(s))
