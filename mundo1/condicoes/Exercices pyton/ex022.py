nome = str(input('Digite seu nome completo:'))

semespacos = nome.replace(' ','')

dividir = nome.split()

print('ola',nome,'!')
print('o seu nome tem ',len(nome) ,'caracteres')
print('O seu nome em maiusculas fica',nome.upper())
print('o seu nome em minusculas fica',nome.lower())
print('o seu nome sem espacos fica com',len(semespacos) ,'caracteres')
print('o seu primeiro nome dividido fica', dividir[0] ,'e tem', len(dividir[0]), 'letras')    