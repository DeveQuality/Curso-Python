""" Faca um programa que leia tres numeros e mostre qual o maior e qual o menor """

numero1=int(input('Qua o primeiro numero: '))
numero2=int(input('Qua o segundo numero: '))
numero3=int(input('Qua o terceiro numero: '))

maior= max(numero1 , numero2 , numero3)  #funcao max retorna o maior
menor= min(numero1 , numero2 , numero3)  #funcao min retorna o menor


print('os primeiros sao {} , {} ,{}'.format(numero1 ,numero2 , numero3))
print('o maior numero e {} e o menor e {}'.format(maior , menor))