import random

def rolar_dados(n):
    dados = []
    for _ in range(n):
        dados.append(random.randint(1, 6))
    return dados