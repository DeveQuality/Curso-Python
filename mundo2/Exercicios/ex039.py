from datetime import date

ano=int(input('Qual o seu ano de nascimento? '))

data =date.today().year

idade= data-ano

print('a sua idade correspode a {} anos '.format(idade))

if idade >= 18  and idade < 35 :
    print('Ainda vai poder se alistar ao servico militar. Esta faltando {} anos ate o prazo da idade de alistamento!'.format(35-idade))
elif idade == 35:
    print('Ja é hora de se alistar')
elif idade < 18:
    print('Desculpe! ainda esta cedo pra se alistar')
elif idade > 35:
    print('DESCULPE! Ja passou o tempo do alistamento  . Passou {} anos  do prazo de alistamento!'.format(idade-35))

