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


def gerar_lista(tamanho):
    lista = []
    for i in range(tamanho):
        numero = random.randint(1, 1000)
        lista.append(numero)
    return lista

#TESTANDO O ALGORITMO

print("Algoritmo Bubble Sort")
tamanho = 10
numeros = gerar_lista(tamanho)
print("Lista original:", numeros)
comparacoes, trocas = bubble_sort(numeros)
print("Lista ordenada:", numeros)
print("Número de comparações:", comparacoes)
print("Número de trocas:", trocas)