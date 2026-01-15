""" CRIE UM PROGRAMA QUE leia varios numeros inteiros pelo teclado, no final 
    mostre a media entre eles todos os valores e qual foi o maior e menor valores lidos.
    O programa deve perguntar ao usuario se ele quer ou nao continuar a digitar valores """


pergunta='S'
s=0
n=0
lista=[]

while pergunta!='N':
    usuario=int(input('Digite um valor: '))
    pergunta=str(input('Quer continuar?(S/N) ')).upper()

    s+=usuario
    n+=1
    media=s/n
    lista.append(usuario)
    

    maior=max(lista)
    menor=min(lista)

print('\033[33m 💻Temos {} valores, com a somatoria de {}, totalizando uma media de {}.'.format(n,s,media))
print('\033[34m O maior valor sera {}'.format(maior))
print('\033[32m O menor valor sera {}'.format(menor))
