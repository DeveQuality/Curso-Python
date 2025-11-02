tipo = input('Digite algo =') 


print('ola Benny isso e uma',  type(tipo))
print('tem espaços ?' , tipo.isspace())
print('is a number ?' , tipo.isnumeric())
print('is alphabetic ?' , tipo.isalpha())
print('is alphanumeric ?', tipo.isalnum())
print('estao em maiusculas ?', tipo.isupper())
print('estao em minusculos ?', tipo.islower())
print('esta capitalizada ?' , tipo.istitle())