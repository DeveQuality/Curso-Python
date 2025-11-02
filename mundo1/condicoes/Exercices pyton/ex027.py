nome=str(input('Digite o seu nome completo: ')).strip()

dividir=nome.split()

print(dividir)
print('Seu primeiro nome:', dividir[0])
print('Seu ultimo nome', dividir[-1])