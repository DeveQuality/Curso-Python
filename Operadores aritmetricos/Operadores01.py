""" nome = input('qual o seu nome?')
print ('Prazer em te conhecer{:20}!'.format(nome) ) """
n1 = int(input('One Value: '))
n2 = int(input('Another Value: '))

soma = n1+n2
mult = n1*n2
div  = n1/n2
di   = n1//n2
exp  = n1**n2

print('A Soma vale {}, \n a multiplicaçao e {}, \n  a divisao e {} , \n  a divisao inteira e {} , \n e a exponeciacao e de {} ' .format(soma,mult,div,di,exp))