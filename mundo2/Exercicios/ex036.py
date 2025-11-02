casa=float(input('Qual o valor da casa: '))
salario=float(input('Qual o seu salario: '))
anos=int(input('Em quantos anos vai pagar: '))

porcentagem=salario * 30/100

parcela=casa/(anos*12)

    
print('Os trinta porcentos do teu salario sao {}mzn,'.format(porcentagem))

print('Caro Cliente , vai ter que pagar {}mzn por ano '.format(parcela))  

if parcela <= porcentagem:
    print('Caro cliente , vai poder comprar a casa , conforme a parcela')
else:
    print('Caro Cliente , nao vai poder comprar a casa pois a parcela é menor que a porcentagem') 

