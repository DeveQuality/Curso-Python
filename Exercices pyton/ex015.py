# Escreva um programa que pergunta a quantidade de km percorridos por carro e a quantidade de dias pelos quais ela foi alugado.Calcule o preco a pagar, sabendo que o carro custa 60 mzn por dia e 0.15 por km rodado
dias = int(input('how many days rent '))
km = float(input('how many km drove '))

pago= (dias*60) + (km * 0.15)

print('you have to pay {:.2f}mzn' .format(pago))