from time import sleep

nome=str(input('Escreva uma frase: ')).replace(' ','').lower()

for b in range(1):

    invertido=nome[::-1]
    normal=invertido[::-1]

    print(' ⏳ invertido sera {}'.format(invertido))
    print(' ⌛ e normal sera {}'.format(normal))
    sleep(1)

    if invertido==normal:
        print('🎇 palidromo')
    else:
        print(' ☹ Nao é palidromo')
print('\033[31m Fim!')
