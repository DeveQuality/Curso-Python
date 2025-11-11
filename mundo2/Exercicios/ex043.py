peso=float(input('Qual o seu peso (kg): '))
altura=float(input('Qual a sua altura (m): '))

imc= peso / (altura**2)

print('-----RESULTADO-------------------------------------------------')

print('O seu imc é {:.3f}'.format(imc))

if imc < 18.5 :
    print('Abaixo do peso')

elif imc > 18.5 and imc < 25 :
    print('Peso ideal')

elif imc > 25 and imc < 30 :
    print('Sobrepeso')

elif imc > 30 and imc < 40 :
    print('Obesidade')

elif imc > 40 :
    print('Obesidade morbida')


""" 
IMC-Indice de Massa Corporal
"""