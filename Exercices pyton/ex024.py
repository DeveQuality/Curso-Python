morada=str(input('Digite a sua cidade : ')).strip()     

print(morada[:3].upper() == 'Moz')

"""
!  strip no final  vai tirar os espacos 
*   entao na linha do print o morada[:3] vai se responsabilizar que a palavra que o usuario vai digitar tenha do inicio ate 3 caracteres ,e mesmo com juncao de letras maiusculas e minusculas seja aceite sendo a palavra Moz 

"""




""" morada = str(input('Qual é o seu pais? '))

pais=morada.startswith('Moçambique')

if morada != 'Moçambique':
    print('Voce nao é moçambicano , seja bem vindo a Moçambique!')
else:
    print('Voce é moçambicano ,bem vindo de vola!')  """