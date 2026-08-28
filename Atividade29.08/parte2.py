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


def gerar_lista(tamanho):
    lista = []
    for i in range(tamanho):
        numero = random.randint(1, 1000)
        lista.append(numero)
    return lista


def testar_tamanho(tamanho):
    original = gerar_lista(tamanho)

    copia_bubble = original.copy()
    comp_bubble, troca_bubble = bubble_sort(copia_bubble)

    _, comp_quick, mov_quick = quicksort(original)

    print(f"{tamanho:<10} | {comp_bubble:<20} | {troca_bubble:<15} | "
          f"{comp_quick:<20} | {mov_quick:<20}")


def main():
    print(f"{'Tamanho':<10} | {'Bubble-Comparacoes':<20} | {'Bubble-Trocas':<15} | "
          f"{'Quick-Comparacoes':<20} | {'Quick-Movimentacoes':<20}")

    for tamanho in (10, 20, 1000):
        testar_tamanho(tamanho)


if __name__ == "__main__":
    main()