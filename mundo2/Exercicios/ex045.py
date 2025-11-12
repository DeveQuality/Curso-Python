import random

print("🎮 Jogo: Pedra, Papel ou Tesoura")

# Entrada do jogador
jogador = input("Escolha (pedra, papel ou tesoura): ").lower()

# Geração aleatória para o computador
numero = random.randint(1, 3)

if numero == 1:
    computador = "pedra"
elif numero == 2:
    computador = "papel"
elif numero == 3:
    computador = "tesoura"

print("O computador escolheu:", computador)

# Verificação das jogadas
if jogador == computador:
    print("🤝 Empate!")

elif jogador == "pedra":
    if computador == "tesoura":
        print("✅ Você ganhou!")
    elif computador == "papel":
        print("💻 O computador ganhou!")
    else:
        print("❌ Escolha inválida.")

elif jogador == "papel":
    if computador == "pedra":
        print("✅ Você ganhou!")
    elif computador == "tesoura":
        print("💻 O computador ganhou!")
    else:
        print("❌ Escolha inválida.")

elif jogador == "tesoura":
    if computador == "papel":
        print("✅ Você ganhou!")
    elif computador == "pedra":
        print("💻 O computador ganhou!")
    else:
        print("❌ Escolha inválida.")

else:
    print("❌ Escolha inválida! Digite pedra, papel ou tesoura.")
