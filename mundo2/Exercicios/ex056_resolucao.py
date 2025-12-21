soma_idade=0
maior_idade_homen=0
nome_velho=0
mulheres=0

for b in range(1,5):
    print('--------{}° pessoa-----------'.format(b))
    nome=str(input('Nome: '))
    idade=int(input('Idade: '))
    sexo=str(input('Sexo[m/f]: ')).lower()

    soma_idade=soma_idade+idade

    if b == 1 and sexo in 'Mm':
        maior_idade_homen=idade
        nome_velho=nome

    if sexo in 'Mm' and idade>maior_idade_homen:
        maior_idade_homen=idade
        nome_velho=nome
        
    if sexo == 'f' and idade<20:
        mulheres+=1

media_idade=soma_idade/4

print('A media de idade do grupo sera de :{}'.format(media_idade ))
print('O homen mais velho tem {} anos e se chama {}'.format(maior_idade_homen,nome_velho))
print('Temos {} mulher/es com menos de 20 anos'.format(mulheres))