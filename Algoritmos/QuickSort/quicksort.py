def quicksort(lista):
    if len(lista) <= 1:
        return lista, 0, 0  # lista, comparações, movimentações

    comparacoes = 0
    movimentacoes = 0

    menores = []
    maiores = []
    pivo = lista[-1]

    for elemento in lista[:-1]:
        comparacoes += 1
        if elemento < pivo:
            menores.append(elemento)
            movimentacoes += 1
        else:
            maiores.append(elemento)
            movimentacoes += 1

    lista_menores, comp_menores, mov_menores = quicksort(menores)
    lista_maiores, comp_maiores, mov_maiores = quicksort(maiores)

    lista_ordenada = lista_menores + [pivo] + lista_maiores
    total_comparacoes = comparacoes + comp_menores + comp_maiores
    total_movimentacoes = movimentacoes + mov_menores + mov_maiores

    return lista_ordenada, total_comparacoes, total_movimentacoes
