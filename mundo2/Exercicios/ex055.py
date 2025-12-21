""" primeiro atribuimos uma lista vazia """
lista=[]

for b in range(1,6):
    peso=float(input('Diga o {}° peso: '.format(b)))

    """ aqui adicionamos a variavel peso dentro da lista """
    lista.append(peso)

    """ aqui criamos variaveis para selecionar o maior e menor valor """
    maior=max(lista)
    menor=min(lista)

print('o maior peso sera: {}'.format(maior))
print('o menor peso sera: {}'.format(menor))
