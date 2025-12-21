n1=int(input('Primeiro numero: '))
n2=int(input('Segundo numero: '))

start=1
while start>0:
    print('-------------------------------------Resultado--------------------------------------')
    escolha=int(input(' [1]Somar \n [2]Multiplicar \n [3]Maior \n [4]Novos numeros \n [5]Sair do programa \nEscolha: '))
    print('-------------------------------------Resultado--------------------------------------')
    if start!=5:
        if escolha==1:
            soma=n1+n2
            print('A soma sera de {}'.format(soma))
        if escolha==2:
            multiplicar=n1*n2
            print('A multiplicacao dos dois valores sera de {}'.format(multiplicar))
        if escolha==3:
            maior=max(n1,n2)
            print('O maior valor sera {}'.format(maior))


        if escolha==4:
            Nv_1=int(input('digite um novo numero: '))
            Nv_2=int(input('digite um novo numero: '))

            if escolha==1:
                soma2=Nv_1+Nv_2
                print('A soma sera de {}'.format(soma2))
            if escolha==2:
                multiplicar2=Nv_1*Nv_2
                print('A multiplicacao dos dois valores sera de {}'.format(multiplicar2))
            if escolha==3:
                maior2=max(Nv_1,Nv_2)
                print('O maior valor sera {}'.format(maior2))
