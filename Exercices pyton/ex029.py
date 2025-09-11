velocidade = int(input('Qual a sua velocidade: '))

multa = 7*velocidade

if velocidade >= 80:
    print('sua velocidade esta em {}km/h , recebeu a uma multa de {}mzn'.format(velocidade,multa))
else:
    print('sua velocidade esta nos {}km/h ,Boa viajem! '.format(velocidade))
