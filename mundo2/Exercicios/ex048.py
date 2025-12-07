s=0
cont=0

for b in range (0 , 500):
    if b%2==1 and b%3==0:
        s=s+b
        cont=cont+1
        print(b)

print('sao {} valores ,serao somados somente esses valores'.format(cont))
print('a soma dos valores impares e divisiveis de 3 é: {}.'.format(s))