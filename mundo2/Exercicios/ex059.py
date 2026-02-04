""" n1=int(input('Primeiro numero: '))

n2=int(input('Segundo numero: '))

escolha=1
while escolha!=5:
    print('-------------------------------------Resultado--------------------------------------')
    escolha=int(input(' [1]Somar \n [2]Multiplicar \n [3]Maior \n [4]Novos numeros \n [5]Sair do programa \nEscolha: '))
    print('-------------------------------------Resultado--------------------------------------')
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
        Nv_1=int(input('digite um primeiro novo numero: '))
        Nv_2=int(input('digite um segundo novo numero: '))
        
        print('-------------------------------------Resultado_2--------------------------------------')
        escolha_2=int(input(' [1]Somar \n [2]Multiplicar \n [3]Maior \n [4]Novos numeros \n [5]Sair do programa \nEscolha: '))
        print('-------------------------------------Resultado_2--------------------------------------')

        if escolha_2==1:
            soma2=Nv_1+Nv_2
            print('A soma sera de {}'.format(soma2))
        if escolha_2==2:
            multiplicar2=Nv_1*Nv_2
            print('A multiplicacao dos dois valores sera de {}'.format(multiplicar2))
        if escolha_2==3:
            maior2=max(Nv_1,Nv_2)
            print('O maior valor sera {}'.format(maior2))

print('Fim do programa...')
 """

n1=int(input('Primeiro numero: '))
n2=int(input('Segundo numero: '))

opcao=0
while opcao!=5:
    print('''    [1]somar
    [2]multiplicar
    [3]maior
    [4]novos numeros
    [5]sair do programa''')
    opcao=int(input('>>>>>>>Qual a sua opcao?:'))

    if opcao==1:
        soma=n1+n2
        print('A soma entre {} e {} sera de {}'.format(n1,n2,soma))
    elif opcao==2:
        multiplicar=n1*n2
        print('A multiplicacao entre {} e {} sera de {}'.format(n1,n2,multiplicar))
    elif opcao==3:
        maior=max(n1,n2)
        print('O maior numero entre {} e {} sera de {}'.format(n1,n2,maior))
    elif opcao==4:
        print('Informe novos numeros:')
        n1=int(input('Primeiro numero: '))
        n2=int(input('Segundo numero: '))
    elif opcao==5:
        print('Finalizando...')
    else:
        print('Opcao invalida ,tente novamente!')
    print('=-='*10)

print('Fim do programa')