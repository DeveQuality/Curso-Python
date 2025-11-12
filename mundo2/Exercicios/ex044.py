Preco=float(input('Qual o preco do produto: '))

print('''
Metodo de pagamento:
[1] Dinheiro/Cheque
[2] Cartao
[3] 2x no cartao
[4] 3x ou mais no cartao
''')

Pagamento=int(input('Qual o metodo de pagamento: '))

ChequeDinheiro = Preco * 10/100
Cartao = Preco *  5/100
juro=Preco * 20/100

print('--------RESULTADO-----------------------------------------------------')

if Pagamento == 1 :
    print('Recebeu 10% de desconto . Custo:{}MZN'.format(Preco - ChequeDinheiro))
    
elif Pagamento == 2 :
    print('Recebeu 5% de desconto . Custo:{}MZN'.format(Preco - Cartao))
    
elif Pagamento == 3 :
    total=Preco
    parcela= total / 2
    print('Preco sem desconto . Custo:{}MZN'.format(parcela))
    
elif Pagamento == 4 :
    total=Preco+(Preco*20/100)
    totalparcela=int(input('Quantas parcelas: '))
    parcela= total / totalparcela
    print(' Sua compra no cartao sera parcelada {}x de {:.2f}MZN'.format(totalparcela,parcela))
    
else:
    print('Desculpe! Opcao invalida de pagamento.')
