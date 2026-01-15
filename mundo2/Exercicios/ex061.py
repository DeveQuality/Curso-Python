pt=int(input('digite o primeiro termo: '))
r=int(input('digite a razao: '))

termo=pt
contador=1

while contador<=10:
    print(termo,end='...')
    termo+=r
    contador+=1

print('fim')