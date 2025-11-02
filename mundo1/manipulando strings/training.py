import random

def gerar_numeros():
    # Sorteia 6 números únicos entre 1 e 60 (como na Mega-Sena, por exemplo)
    numeros = random.sample(range(1, 61), 6)
    return sorted(numeros)

# Executando
print("Seus 6 números sorteados são:", gerar_numeros())
