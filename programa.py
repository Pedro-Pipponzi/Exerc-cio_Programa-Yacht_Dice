from funcoes import (rolar_dados, guardar_dado, remover_dado, faz_jogada, imprime_cartela)


def ehinteiro(s):
    if len(s) == 0:
        return False
    for c in s:
        if c < "0" or c > "9":
            return False
    return True


def novacartela():
    return {
        "regra_simples": {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1},
        "regra_avancada": {
            "sem_combinacao": -1,
            "quadra": -1,
            "full_house": -1,
            "sequencia_baixa": -1,
            "sequencia_alta": -1,
            "cinco_iguais": -1
        }
    }


def preenchida(cartela, combo):
    if ehinteiro(combo):
        n = int(combo)
        if n in cartela["regra_simples"]:
            return cartela["regra_simples"][n] != -1
        return False
    if combo in cartela["regra_avancada"]:
        return cartela["regra_avancada"][combo] != -1
    return False


def existe(cartela, combo):
    if ehinteiro(combo):
        return int(combo) in cartela["regra_simples"]
    return combo in cartela["regra_avancada"]


def mostra(rolados, guardados):
    print(f"Dados rolados: {rolados}")
    print(f"Dados guardados: {guardados}")


def pontuacao(cartela):
    simples = 0
    for v in cartela["regra_simples"].values():
        if v != -1:
            simples += v
    avancada = 0
    for v in cartela["regra_avancada"].values():
        if v != -1:
            avancada += v
    bonus = 35 if simples >= 63 else 0
    return simples + avancada + bonus


def jogo():
    cartela = novacartela()
    imprime_cartela(cartela)

    for _ in range(12):
        rolados = rolar_dados(5)
        guardados = []
        rerrolagens = 0
        feita = False
        status = True

        while not feita:
            if status:
                mostra(rolados, guardados)
                print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            status = True
            opcao = input()

            if opcao == "1":
                print("Digite o índice do dado a ser guardado (0 a 4):")
                g = input()
                if ehinteiro(g) and 0 <= int(g) < len(rolados):
                    resultado = guardar_dado(rolados, guardados, int(g))
                    rolados = resultado[0]
                    guardados = resultado[1]

            elif opcao == "2":
                print("Digite o índice do dado a ser removido (0 a 4):")
                g = input()
                if ehinteiro(g) and 0 <= int(g) < len(guardados):
                    resultado = remover_dado(rolados, guardados, int(g))
                    rolados = resultado[0]
                    guardados = resultado[1]

            elif opcao == "3":
                if rerrolagens >= 2:
                    print("Você já usou todas as rerrolagens.")
                else:
                    nrolar = 5 - len(guardados)
                    rolados = rolar_dados(nrolar)
                    rerrolagens += 1

            elif opcao == "4":
                imprime_cartela(cartela)

            elif opcao == "0":
                dados = rolados + guardados
                print("Digite a combinação desejada:")
                valida = False
                while not valida:
                    combo = input()
                    if not existe(cartela, combo):
                        print("Combinação inválida. Tente novamente.")
                    elif preenchida(cartela, combo):
                        print("Essa combinação já foi utilizada.")
                    else:
                        cartela = faz_jogada(dados, combo, cartela)
                        valida = True
                        feita = True

            else:
                print("Opção inválida. Tente novamente.")
                status = False

    imprime_cartela(cartela)
    total = pontuacao(cartela)
    print(f"Pontuação total: {total}")


jogo()
