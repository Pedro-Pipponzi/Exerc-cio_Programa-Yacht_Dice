import random

#1
def rolar_dados(n):
    dados = []
    for _ in range(n):
        dados.append(random.randint(1, 6))
    return dados

#2
def guardar_dado(rolados, estoque, guardar):
    dado = rolados[guardar]
    novorolados = []
    for i in range(len(rolados)):
        if i != guardar:
            novorolados.append(rolados[i])
    estoque.append(dado)
    return [novorolados, estoque]

#3
def remover_dado(dados_rolados, dados_estoque, remover):
    dado = dados_estoque[remover]
    novo_estoque = []
    for i in range(len(dados_estoque)):
        if i != remover:
            novo_estoque.append(dados_estoque[i])
    dados_rolados.append(dado)
    return [dados_rolados, novo_estoque]

#4
def calcula_pontos_regra_simples(lista):
    dicio = {}
    for face in range(1, 7):
        pontos = 0
        for dado in lista:
            if dado == face:
                pontos += face
        dicio[face] = pontos
    return dicio

#5
def calcula_pontos_soma(lista):
    pontuacao = 0
    for dado in lista:
        pontuacao += dado
    return pontuacao

#6
def calcula_pontos_sequencia_baixa(lista):
    lista2 = sorted(set(lista))
    i = 0
    for j in range(1, len(lista2)):
        if lista2[j] == lista2[j-1] + 1:
            i += 1
            if i >= 3:
                return 15
        else:
            i = 0
    
    return 0