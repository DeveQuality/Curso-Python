""" crie um programa que leia varios numeros inteiros pelo teclado .
    o programa so vai parar quando o usuario digitar 999 
    que sera a codicao de parada no final mostra quantos numeros
    foram digitados e qual foi a soma entre eles (desconsiderando o flag) """

n=1
numeros=0
soma=0
while n != 999:
    n=int(input('Digite um numero: '))
    if n != 999:
        numeros+=1
        soma=soma+n

print('Foram digitados {} numeros'.format(numeros))
print('E a soma de todos valores sera de {}'.format(soma))