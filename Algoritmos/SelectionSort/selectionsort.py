def selection_sort(lista):
    n = len(lista)
    comparacoes = 0
    trocas = 0
    for i in range(n - 1):
        indice_menor = i
        for j in range(i + 1, n):
            comparacoes += 1
            if lista[j] < lista[indice_menor]:
                indice_menor = j
        if indice_menor != i:
            lista[i], lista[indice_menor] = lista[indice_menor], lista[i]
            trocas += 1
    return comparacoes, trocas
