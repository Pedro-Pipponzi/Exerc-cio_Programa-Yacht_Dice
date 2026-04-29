import random

def rolar_dados(n):
    dados = []
    for _ in range(n):
        dados.append(random.randint(1, 6))
    return dados

def guardar_dado(rolados, estoque, guardar):
    dado = rolados[guardar]
    novorolados = []
    for i in range(len(rolados)):
        if i != guardar:
            novorolados.append(rolados[i])
    estoque.append(dado)
    return [novorolados, estoque]