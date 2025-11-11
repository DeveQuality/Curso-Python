from datetime import date

data=date.today().year

ano=int(input('Digite o seu ano de Nascimento '))

Ano = data - ano

print('Tens {} anos e ...' .format(Ano))

if Ano < 9:
    print('O Seu nivel de nataçao é  MIRIM') 

elif Ano > 9 and Ano < 14:
    print('O Seu nivel de nataçao é INFANTIL')

elif Ano > 14 and Ano < 19:
    print('O Seu nivel de nataçao é JUNIOR')

elif Ano > 19 and Ano < 25:
    print('O Seu nivel de nataçao é SENIOR')

elif Ano > 20:
    print('O Seu nivel de nataçao é  Master')

