import subprocess

while True:
    print("=== Atividades Avaliativas - Estruturas de Dados II ===\n")
    print("--- Atividade 2: Arrays, Matrizes, Ordenação e Busca ---")
    print("1 - Parte 2 (Ordenação)")
    print("2 - Parte 3 (Busca em Matriz)")
    print("3 - Parte 4 (Hands On 1)")
    print("4 - Parte 5 (Hands On 2)")
    print("\n--- Atividade 3: Ordenação (Central de Distribuição) ---")
    print("5 - Experimento de Ordenação (Bubble, Insertion, Selection, Quick)")
    print("6 - Desafio Adicional (aleatório x ordenado x invertido)")
    print("\n--- Atividade 4: Sistema de Atendimento com Filas ---")
    print("7 - Simulação completa (Fila Clássica, Circular, Prioridade + Desafio)")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        subprocess.run(["python", "Atividade_2_ArraysMatrizes/Parte2_Ordenacao/parte2.py"])
    elif opcao == "2":
        subprocess.run(["python", "Atividade_2_ArraysMatrizes/Parte3_BuscaMatriz/parte3.py"])
    elif opcao == "3":
        subprocess.run(["python", "Atividade_2_ArraysMatrizes/Parte4_HandsOn1/parte4.py"])
    elif opcao == "4":
        subprocess.run(["python", "Atividade_2_ArraysMatrizes/Parte5_HandsOn2/parte5.py"])
    elif opcao == "5":
        subprocess.run(["python", "Atividade_3_Ordenacao/experimento_ordenacao.py"])
    elif opcao == "6":
        subprocess.run(["python", "Atividade_3_Ordenacao/desafio_adicional.py"])
    elif opcao == "7":
        subprocess.run(["python", "Atividade_4_Filas/Atendimento_com_Filas/atividade_4.py"])
    elif opcao == "0":
        print("Encerrando...")
        break
    else:
        print("Opção inválida.")
