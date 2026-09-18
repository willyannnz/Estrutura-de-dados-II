import random


def bubble_sort(lista):
    """Comparação = todo teste lista[j] > lista[j+1]. Troca = toda troca de posição efetiva."""
    n = len(lista)
    comparacoes = 0
    trocas = 0
    for i in range(n - 1):
        for j in range(n - 1 - i):
            comparacoes += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas += 1
    return comparacoes, trocas


def selection_sort(lista):
    """Comparação = todo teste lista[j] < lista[indice_menor]. Troca = uma troca por
    passada externa, apenas quando o menor elemento encontrado não é o já posicionado."""
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


def insertion_sort(lista):
    """Comparação = todo teste lista[j] > chave. Movimentação = todo deslocamento de um
    elemento uma posição à direita para abrir espaço para a chave (não conta a inserção
    final da chave em si, apenas os deslocamentos)."""
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


def quicksort(lista):
    """Comparação = todo teste elemento < pivo. Movimentação = toda inserção de um
    elemento em uma das listas auxiliares (menores/maiores)."""
    if len(lista) <= 1:
        return lista, 0, 0

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


def gerar_lista(tamanho):
    lista = []
    for i in range(tamanho):
        numero = random.randint(1, 1000)
        lista.append(numero)
    return lista


def testar_tamanho(tamanho):
    original = gerar_lista(tamanho)

    vetor_bubble = original.copy()
    vetor_insertion = original.copy()
    vetor_selection = original.copy()
    vetor_quick = original.copy()

    comp_bubble, troca_bubble = bubble_sort(vetor_bubble)
    comp_insertion, mov_insertion = insertion_sort(vetor_insertion)
    comp_selection, troca_selection = selection_sort(vetor_selection)
    _, comp_quick, mov_quick = quicksort(vetor_quick)

    print(f"\n{'-'*65}")
    print(f" TAMANHO DO VETOR: {tamanho}")
    print(f"{'-'*65}")
    print(f"{'Algoritmo':<18} | {'Comparações':<15} | {'Movimentações/Trocas':<20}")
    print(f"{'-'*65}")
    print(f"{'Bubble Sort':<18} | {comp_bubble:<15} | {troca_bubble:<20}")
    print(f"{'Insertion Sort':<18} | {comp_insertion:<15} | {mov_insertion:<20}")
    print(f"{'Selection Sort':<18} | {comp_selection:<15} | {troca_selection:<20}")
    print(f"{'Quick Sort':<18} | {comp_quick:<15} | {mov_quick:<20}")
    print(f"{'-'*65}")


def main():
    for tamanho in (10, 20, 1000):
        testar_tamanho(tamanho)


if __name__ == "__main__":
    main()