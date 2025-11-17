import random

jogador=int(input(''' Faca sua Escolha : 
    [0] pedra
    [1] papel
    [2] tesoura 
'''))

itens=('pedra','papel','tesoura')

computador=random.randint(0,2)

print('💻 escolheu {}' .format(itens[computador]))
print('😎 voce escolheu {} '.format(itens[jogador]))



if computador == 0:                    
    if jogador == 0:
        print('🤝 Empate')
    elif jogador == 1:
        print('😎 voce Venceu')
    elif jogador == 2:
        print('💻 Computador Venceu')


elif computador == 1:   
    if jogador == 1:
        print('🤝 Empate')
    elif jogador == 0:
        print('💻 compuatdor venceu')
    elif jogador == 2:
        print('😎 Voce ganhou')

        
elif computador == 2:
    if jogador == 2:
        print('🤝 Empate')
    elif jogador == 0:
        print('😎 voce venceu')
    elif jogador == 1:
        print('💻 computador venceu')

else:
    print('❌ Opcao invalida ! Escolha Pedra , Papel ou Tesoura')