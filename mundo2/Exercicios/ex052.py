num=int(input('digite um numero: '))
tot=0

for b in range (1,num+1):
    if num%b==0:
        print('\033[34m', end=" ")
        tot=tot+1                  
    else :
        print('\033[31m', end=" ")
    print(b,end=" ")
print(' \n \033[m O numero {} foi divisivel {} vezes'.format(num , tot))


if tot==2:
    print('Numero primo')
else:
    print('Numero nao primo')



""" 

\033[34m   - sao cores em python(azul)
\033[35m   - cor de rosa
\033[35m   - cor amarela
\033[31m   - cor vermelha

 """