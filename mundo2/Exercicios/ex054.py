from datetime import date

comp_ano=date.today().year
totmaior = 0
totmenor=0

for b in range(1,8):
    ano=int(input('digite o {}° ano de nascimento: '.format(b)))

    calcular=comp_ano-ano

    if calcular >= 21:
        totmaior=totmaior+1
    else:
        totmenor=totmenor+1

print('as maiores de idade são : {} pessoa/as'.format(totmenor))
print('e as menores de idade são : {} pessoa/as'.format(totmenor))

print('fim')
