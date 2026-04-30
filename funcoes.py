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

def remover_dado(dados_rolados, dados_estoque, remover):
    dado = dados_estoque[remover]
    novo_estoque = []
    for i in range(len(dados_estoque)):
        if i != remover:
            novo_estoque.append(dados_estoque[i])
    dados_rolados.append(dado)
    return [dados_rolados, novo_estoque]

def calcula_pontos_regra_simples(lista):
    dicio = {}
    for face in range(1, 7):
        pontos = 0
        for dado in lista:
            if dado == face:
                pontos += face
        dicio[face] = pontos
    return dicio
