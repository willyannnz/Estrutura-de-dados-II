import subprocess

while True:
    print("\n=== Atividades Avaliativas - Estruturas de Dados II ===")
    print("--- Atividade 2 ---")
    print("1 - Parte 2 (Ordenação)")
    print("2 - Parte 3 (Busca em Matriz)")
    print("3 - Parte 4 (Hands On 1)")
    print("4 - Parte 5 (Hands On 2)")
    print("--- Atividade 3 ---")
    print("5 - Experimento de Ordenação (Bubble, Insertion, Selection, Quick)")
    print("6 - Desafio Adicional (aleatório x ordenado x invertido)")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        subprocess.run(["python", "Atividade_2/Parte2_Ordenacao/parte2.py"])
    elif opcao == "2":
        subprocess.run(["python", "Atividade_2/Parte3_BuscaMatriz/parte3.py"])
    elif opcao == "3":
        subprocess.run(["python", "Atividade_2/Parte4_HandsOn1/parte4.py"])
    elif opcao == "4":
        subprocess.run(["python", "Atividade_2/Parte5_HandsOn2/parte5.py"])
    elif opcao == "5":
        subprocess.run(["python", "Atividade_3/experimento_ordenacao.py"])
    elif opcao == "6":
        subprocess.run(["python", "Atividade_3/desafio_adicional.py"])
    elif opcao == "0":
        print("Encerrando...")
        break
    else:
        print("Opção inválida.")
