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

#7
def calcula_pontos_sequencia_alta(lista):
    lista2 = sorted(set(lista))
    i = 0
    for j in range(1, len(lista2)):
        if lista2[j] == lista2[j-1] + 1:
            i += 1
            if i >= 4:
                return 30
        else:
            i = 0
    
    return 0

#8
def calcula_pontos_full_house(lista):
    contagen = []
    vistos = []
    for n in lista:
        if n not in vistos:
            contagen.append(lista.count(n))
            vistos.append(n)
    if 2 in contagen and 3 in contagen:
        soma = 0
        for i in lista:
            soma += i
        return soma
    return 0

#9
def calcula_pontos_quadra(lista):
    soma = 0
    for face in range(1, 7):
        contagem = 0
        for dado in lista:
            if dado == face:
                contagem += 1
        if contagem >= 4:
            for dado in lista:
                soma += dado
            return soma
    return 0

#10
def calcula_pontos_quina (lista):
    for face in range(1, 7):
        contagem = 0
        for dado in lista:
            if dado == face:
                contagem += 1
        if contagem >= 5:
            return 50
    return 0


#11
def calcula_pontos_regra_avancada(lista): 
    dicio = {}
    dicio['cinco_iguais'] = calcula_pontos_quina(lista)
    dicio['full_house'] = calcula_pontos_full_house(lista)
    dicio['quadra'] = calcula_pontos_quadra(lista)
    dicio['sem_combinacao'] = calcula_pontos_soma(lista)
    dicio['sequencia_alta'] = calcula_pontos_sequencia_alta(lista)
    dicio['sequencia_baixa'] = calcula_pontos_sequencia_baixa(lista)
    
    return dicio

#12
def faz_jogada(dados, categoria, cartela):
    if categoria in cartela['regra_avancada']:
        resultado = calcula_pontos_regra_avancada(dados)
        cartela['regra_avancada'][categoria] = resultado[categoria]
        return cartela
    
    else:
        categoria = int(categoria)
        resultado = calcula_pontos_regra_simples(dados)
        cartela['regra_simples'][categoria] = resultado[categoria]
    return cartela

#imprimir cartela de pontos
def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)