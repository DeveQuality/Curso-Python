idade=0
Tot_sexo=0

for b in range(1,4):
    nome=str(input('digite o nome da {}° pessoa: '.format(b)))
    idade=int(input('digite a idade da {}° pessoa: ' .format(b)))
    sexo=str(input('digite o sexo da {}° pessoa(f/m): ' . format(b))).lower()

    idade  += idade

    media=idade/3

    if sexo=='f' and idade<20:
        Tot_sexo += 1

print('\033[32m O nome do mais velho 👨‍🦳 sera:  {}' .format())
print('\033[33m A media das idades sera:{}'.format(media))
print('\033[34m Temos {} 👩'.format(Tot_sexo))