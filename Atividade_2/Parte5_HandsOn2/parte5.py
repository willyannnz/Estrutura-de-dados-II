import random


def gerar_matriz_sensores(num_sensores, medicoes_por_sensor):
    """Gera a matriz de sensores com temperaturas aleatórias entre 15 e 32 graus."""
    matriz = []
    for i in range(num_sensores):
        linha = []
        for j in range(medicoes_por_sensor):
            temperatura = round(random.uniform(15.0, 32.0), 1)
            linha.append(temperatura)
        matriz.append(linha)
    return matriz


def calcular_medias_sensores(sensores):
    """Retorna uma lista com a média de cada sensor (cada linha)."""
    medias = []
    for i in range(len(sensores)):
        soma = 0
        for j in range(len(sensores[i])):
            soma += sensores[i][j]
        media = soma / len(sensores[i])
        medias.append(media)
    return medias


def encontrar_maior_temperatura(sensores):
    """Retorna (maior_valor, sensor, hora) percorrendo a matriz inteira."""
    maior_valor = sensores[0][0]
    sensor_do_maior = 0
    hora_do_maior = 0

    for i in range(len(sensores)):
        for j in range(len(sensores[i])):
            if sensores[i][j] > maior_valor:
                maior_valor = sensores[i][j]
                sensor_do_maior = i
                hora_do_maior = j

    return maior_valor, sensor_do_maior, hora_do_maior


def calcular_media_geral(sensores):
    """Soma todas as medições (todas as linhas juntas) e divide pelo total."""
    soma_total = 0
    quantidade_total = 0

    for i in range(len(sensores)):
        for j in range(len(sensores[i])):
            soma_total += sensores[i][j]
            quantidade_total += 1

    return soma_total / quantidade_total


def contar_acima_do_limite(sensores, limite):
    """Conta quantas medições, na matriz inteira, ficaram acima do limite."""
    contador = 0
    for i in range(len(sensores)):
        for j in range(len(sensores[i])):
            if sensores[i][j] > limite:
                contador += 1
    return contador


def main():
    num_sensores = 5
    medicoes_por_sensor = 24

    sensores = gerar_matriz_sensores(num_sensores, medicoes_por_sensor)

    print("--- Matriz de sensores (5 sensores x 24 horas) ---")
    for i, linha in enumerate(sensores):
        print(f"Sensor {i}: {linha}")

    medias = calcular_medias_sensores(sensores)
    print("\n--- Média de cada sensor ---")
    for i, media in enumerate(medias):
        print(f"Sensor {i}: {media:.2f}")

    maior_valor, sensor_do_maior, hora_do_maior = encontrar_maior_temperatura(sensores)
    print(f"\nMaior temperatura registrada: {maior_valor}")
    print(f"Sensor responsável: {sensor_do_maior}")
    print(f"Horário da ocorrência: {hora_do_maior}h")

    media_geral = calcular_media_geral(sensores)
    print(f"\nMédia geral (todas as {num_sensores * medicoes_por_sensor} medições): {media_geral:.2f}")

    limite = float(input("\nDigite um limite de temperatura: "))
    quantidade_acima = contar_acima_do_limite(sensores, limite)
    print(f"Quantidade de leituras acima de {limite}°C: {quantidade_acima}")

    total_posicoes = num_sensores * medicoes_por_sensor
    print(f"\nTotal de posições percorridas na matriz: {total_posicoes}")


if __name__ == "__main__":
    main()
