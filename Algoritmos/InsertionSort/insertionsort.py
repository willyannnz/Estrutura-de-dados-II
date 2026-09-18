def insertion_sort(lista):
    n = len(lista)
    comparacoes = 0
    movimentacoes = 0
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0:
            comparacoes += 1
            if lista[j] > chave:
                lista[j + 1] = lista[j]
                movimentacoes += 1
                j -= 1
            else:
                break
        lista[j + 1] = chave
    return comparacoes, movimentacoes
