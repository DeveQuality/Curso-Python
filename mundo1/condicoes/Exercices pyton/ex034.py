""" Escreva um que pergunte o salario de um funcinario e calcule o valor do seu aumento
-para salarios superiores a 1.250 mzn calcule um aumento de 10%
-para os inferiores ou iguais sera de 15% 
 """
salario=float(input('qual e o seu salario: '))

aumento=(salario*0.10)+salario 
inferiores=(salario*0.15)+salario 


if salario>1250:
    print('o seu aumento sera de {}mzn, entao o teu salario sobe para {}mzn'.format(salario*0.10, aumento))
else:
    print('o seu aumento sera de {}mzn, entao o teu salario sobe para {}mzn'.format(salario*0.15, inferiores))




"""   Converter 15% em número decimal: 0.15 

      salario × 0,15 = aqui teremos o aumento  
"""