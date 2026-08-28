import random

def bubble_sort(lista):
    n = len(lista)
    comparacoes = 0
    trocas = 0
    for i in range(n - 1):
        for j in range(n - 1 - i):
            comparacoes += 1
            if lista[j] > lista[j + 1]:
                # troca de elementos nas posições j e j + 1
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas += 1
    return comparacoes, trocas

tamanho = 10
numeros = [random.randint(1, 100) for _ in range(tamanho)]
comparacoes, trocas = bubble_sort(numeros)
print("Lista ordenada:", numeros)
print("Número de comparações:", comparacoes)
print("Número de trocas:", trocas)