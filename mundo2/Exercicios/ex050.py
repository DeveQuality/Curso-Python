s=0
cont=0
for b in range(1 ,7):
    nr=int(input('digite o {}° numero: '.format(b)))
    
    if nr%2==0:
        s= s + nr
        cont=cont+1

print('Temos {} valores e a soma dos valores pares sera de {}'.format(cont,s))
