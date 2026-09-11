def insertion_sort(lista): 
    n = len(lista)
    comparacoes = 0
    trocas = 0
    for i in range(1, n):
        j = i -1
        while j >= 0 and lista[j] > lista[j + 1]:
            comparacoes += 1    
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
            trocas += 1
            j -= 1
        lista[j + 1] = lista[i]
    return lista, comparacoes, trocas