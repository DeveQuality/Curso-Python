from datetime import date

ano=int(input('Digite o ano que você quer analisar , ou se quiser digite 0 para analisar o ano atual: '))

if ano == 0:    
    ano=date.today().year

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('digitou o ano {},e ele e um ano bissexto'.format(ano))
else:
    print('digitou o ano {},e ele e um ano comum' .format(ano)) 