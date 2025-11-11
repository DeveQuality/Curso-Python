num = int(input("Digite um número inteiro: "))

base=int(input("Digite a base para conversão (1 para binário, 2 para octal, 3 para hexadecimal): "))


binario = 1
octal = 2
hexadecimal = 3


if base == binario:
    print(bin(num)[2:])                             # converte para binario

elif base == octal:
    print(oct(num)[2:])                             # converte para octal

elif base == hexadecimal:
    print(hex(num)[2:])                             # converte para hexadecimal
else:
    print("Base inválida! Por favor, escolha 1, 2 ou 3.")



