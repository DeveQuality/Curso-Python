""" 
Desenvolva um programa que :
pergunte a distancia de uma viagem em km;
calcule o preco da passagem cobrando R$0.50 por km para viagens ate 200km 
e R$0.45 para viajem mais longas'. 
"""

distancia=float(input('Distancia percorida : '))

passagem= distancia*0.50

viagemlonga= distancia*0.45

if distancia <= 200 :
    print('Percoreu uma distancia de {}km, a viajem vai custar {}mzn'.format(distancia,passagem))
else:
    print('Percoreu uma distancia de {}km, a passagem vai custar {}mzn'.format(distancia,viagemlonga))
  