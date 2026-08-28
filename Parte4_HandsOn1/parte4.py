def obter_temperaturas(quantidade):
    """Pede ao usuário as temperaturas uma por uma."""
    temperaturas = []
    for i in range(quantidade):
        valor = float(input(f"Digite a temperatura {i + 1}: "))
        temperaturas.append(valor)
    return temperaturas


def calcular_media(temperaturas):
    return sum(temperaturas) / len(temperaturas)


def encontrar_maior(temperaturas):
    """Retorna (maior_valor, indice) percorrendo o array uma vez."""
    maior = temperaturas[0]
    indice_maior = 0
    for i in range(1, len(temperaturas)):
        if temperaturas[i] > maior:
            maior = temperaturas[i]
            indice_maior = i
    return maior, indice_maior


def encontrar_menor(temperaturas):
    """Retorna (menor_valor, indice) percorrendo o array uma vez."""
    menor = temperaturas[0]
    indice_menor = 0
    for i in range(1, len(temperaturas)):
        if temperaturas[i] < menor:
            menor = temperaturas[i]
            indice_menor = i
    return menor, indice_menor


def contar_acima_da_media(temperaturas, media):
    contador = 0
    for temp in temperaturas:
        if temp > media:
            contador += 1
    return contador


def mostrar_temperaturas(temperaturas):
    for i, temp in enumerate(temperaturas):
        print(f"Índice {i}: {temp}")


def main():
    quantidade = 10
    temperaturas = obter_temperaturas(quantidade)

    print("\n--- Temperaturas registradas ---")
    mostrar_temperaturas(temperaturas)

    media = calcular_media(temperaturas)
    maior, indice_maior = encontrar_maior(temperaturas)
    menor, indice_menor = encontrar_menor(temperaturas)
    acima_da_media = contar_acima_da_media(temperaturas, media)

    # Cada função acima percorre o array uma vez (n operações).
    # Chamamos 4 delas (média, maior, menor, contagem) = aproximadamente 4n operações no total.
    operacoes_aproximadas = 4 * quantidade

    print("\n--- Resultados ---")
    print(f"Média: {media:.2f}")
    print(f"Maior valor: {maior} (índice {indice_maior})")
    print(f"Menor valor: {menor} (índice {indice_menor})")
    print(f"Quantidade de valores acima da média: {acima_da_media}")
    print(f"Operações de percurso do array (aproximado): {operacoes_aproximadas}")
    print("Complexidade do algoritmo: O(n) — cada função faz uma única passada pelo array.")


if __name__ == "__main__":
    main()
