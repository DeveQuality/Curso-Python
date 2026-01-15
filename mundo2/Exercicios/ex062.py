pt=int(input('digite o primeiro termo: '))
r=int(input('digite a razao: '))

termo=pt
contador=1

while contador<=10:
    print('{}'.format(termo))
    termo+=r
    contador+=1

usuario=int(input('Digite (1) para continuar ou\nDigite (0) para encerar: '))
while usuario!=0:
    
    pt2=int(input('Digite o primeiro termo: '))
    r2=int(input('Digite a razao: '))
    nr_termos=int(input('Quantos termos quer mostrar: '))

    termo=pt2
    contador=1

    while contador<=nr_termos:
        print(termo)
        termo+=r2
        contador+=1

print('Fim do programa...')
