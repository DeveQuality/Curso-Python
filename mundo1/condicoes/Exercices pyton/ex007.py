nome = str(input('type your name: '))
number1 =int(input('type the first mark: '))
number2 =int(input('type the second mark: '))
number3 =int(input('type the third mark: '))

soma = number1 + number2 + number3
divisao = soma // 3

print('Ola! estudante {} , a soma das tuas notas é {}...' .format(nome,soma))
print('A sua media é {}' .format(divisao))
