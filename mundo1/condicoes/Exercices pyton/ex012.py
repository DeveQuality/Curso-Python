name = str(input('Hi! what is your name ?'))
preco= float(input('what is the product prince : '))

produto = preco - (preco*5/100)

print('hi {} , the product cust {}mt , in promotion of 5% it will cust {}' .format(name,preco,produto) )