""" verificando o valor par e o impar  """


n=1
par=impar=0
while n!=0:
    n=int(input('Type a number: '))
    if n!=0:
        if n%2==0:
            par+=1
        else:
            impar+=1

print('Temos {} numeros pares e {} numeros inpares'.format(par,impar))
print('This is the end!')