def busca_binaria(lista, alvo):
    inicio = 0  # inicio da lista
    fim = len(lista) - 1  # fim da lista
    tentativas = 0  # Contador. Começa em 0 pois ainda não fizemos
    # nenhuma comparação. Se a lista tem 10 elementos, o último índice é 9

    while inicio <= fim:
        # Enquanto ainda existir um intervalo válido de busca.
        # Se inicio passar de fim, significa que o número não está na lista.
        tentativas += 1
        # Cada vez que entramos no loop, vamos olhar o meio e comparar.
        # Isso já conta como uma tentativa.
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return tentativas
        elif lista[meio] < alvo:
            # Se o valor do meio é menor quer o alvo,
            # sabemos que o alvo só pode estar à direita.
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1
