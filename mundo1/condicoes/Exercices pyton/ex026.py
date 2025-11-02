nome=str(input('Digite seu nome: ')).upper().strip()

contar = nome.count('A')

print(contar)
print('o primeiro -a- esta na posicao :', nome.find('A'))
print('o ultimo -a- esta na posicao :', nome.rfind('A'))



""" o .rfind() procura da direita para a esquerda"""