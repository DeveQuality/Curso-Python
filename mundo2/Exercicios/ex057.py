sexo=str(input('Type your gender(m/f): ')).strip()

while sexo !='m' and sexo != 'f':
    sexo=str(input('ERROR! Try again: ')).strip()
if sexo=='f':
    print('You are woman')
elif sexo=='m':
    print('You are Man')
    
print('CORRECT!  This is the end!')
