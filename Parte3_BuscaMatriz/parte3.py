def busca_sequencial(matriz, linhas, colunas, valor):
    comparacoes = 0
    
    for l in range(linhas):
        for c in range(colunas):
            comparacoes += 1
            if matriz[l][c] == valor:
                return True, l, c, comparacoes
                
    # Retorno caso o valor não exista na matriz
    return False, -1, -1, comparacoes


def gerar_matriz(linhas, colunas):
    matriz = []
    contador = 1
    for l in range(linhas):
        linha = []
        for c in range(colunas):
            linha.append(contador)
            contador += 1
        matriz.append(linha)
    return matriz



print(f"{'Matriz':<10} | {'Nº elementos':<12} | {'Busca início':<15} | {'Busca fim':<12} | {'Valor inexistente'}")

tamanhos = [2, 10, 100]

# Laço para rodar os testes automaticamente
for n in tamanhos:
    linhas = n
    colunas = n
    total_elementos = linhas * colunas
    
    matriz = gerar_matriz(linhas, colunas)
    
    # Definindo os alvos da busca
    valor_inicio = matriz[0][0]
    valor_fim = matriz[linhas - 1][colunas - 1]
    valor_inexistente = total_elementos + 1
    
    
    _, _, _, comp_inicio = busca_sequencial(matriz, linhas, colunas, valor_inicio)
    _, _, _, comp_fim = busca_sequencial(matriz, linhas, colunas, valor_fim)
    _, _, _, comp_inexistente = busca_sequencial(matriz, linhas, colunas, valor_inexistente)
    
    # Impressão dos resultados na tabela
    print(f"{n}x{n:<8} | {total_elementos:<12} | {comp_inicio:<15} | {comp_fim:<12} | {comp_inexistente}")