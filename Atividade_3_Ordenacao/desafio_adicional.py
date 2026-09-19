import sys
sys.setrecursionlimit(10000)

import random


def bubble_sort(lista):
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


def gerar_vetor_aleatorio(tamanho):
    return [random.randint(1, 1000) for _ in range(tamanho)]


def gerar_vetor_ordenado(tamanho):
    return list(range(1, tamanho + 1))


def gerar_vetor_invertido(tamanho):
    return list(range(tamanho, 0, -1))


def testar_vetor(nome, vetor_original):
    vetor_bubble = vetor_original.copy()
    vetor_insertion = vetor_original.copy()
    vetor_selection = vetor_original.copy()
    vetor_quick = vetor_original.copy()

    comp_bubble, troca_bubble = bubble_sort(vetor_bubble)
    comp_insertion, mov_insertion = insertion_sort(vetor_insertion)
    comp_selection, troca_selection = selection_sort(vetor_selection)
    _, comp_quick, mov_quick = quicksort(vetor_quick)

    print(f"\n{'-'*65}")
    print(f" ESTADO DO VETOR: {nome.upper()} (Tamanho: {len(vetor_original)})")
    print(f"{'-'*65}")
    print(f"{'Algoritmo':<18} | {'Comparações':<15} | {'Movimentações/Trocas':<20}")
    print(f"{'-'*65}")
    print(f"{'Bubble Sort':<18} | {comp_bubble:<15} | {troca_bubble:<20}")
    print(f"{'Insertion Sort':<18} | {comp_insertion:<15} | {mov_insertion:<20}")
    print(f"{'Selection Sort':<18} | {comp_selection:<15} | {troca_selection:<20}")
    print(f"{'Quick Sort':<18} | {comp_quick:<15} | {mov_quick:<20}")
    print(f"{'-'*65}")


def main():
    tamanho = 1000
    testar_vetor("Aleatório", gerar_vetor_aleatorio(tamanho))
    testar_vetor("Ordenado", gerar_vetor_ordenado(tamanho))
    testar_vetor("Invertido", gerar_vetor_invertido(tamanho))


if __name__ == "__main__":
    main()