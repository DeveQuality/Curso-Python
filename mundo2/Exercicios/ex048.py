s=0

for b in range (0 , 500):
    if b%2==1 and b%3==0:
        s=s+b
        print(b)
print('a soma dos valores impares e multiplos de 3 é: {}.'.format(s))