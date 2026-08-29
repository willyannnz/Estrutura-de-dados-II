import subprocess

while True:
    print("\n=== Atividade Avaliativa - Estruturas de Dados II ===")
    print("1 - Parte 2 (Ordenação)")
    print("2 - Parte 3 (Busca em Matriz)")
    print("3 - Parte 4 (Hands On 1)")
    print("4 - Parte 5 (Hands On 2)")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        subprocess.run(["python", "Parte2_Ordenacao/parte2.py"])
    elif opcao == "2":
        subprocess.run(["python", "Parte3_BuscaMatriz/parte3.py"])
    elif opcao == "3":
        subprocess.run(["python", "Parte4_HandsOn1/parte4.py"])
    elif opcao == "4":
        subprocess.run(["python", "Parte5_HandsOn2/parte5.py"])
    elif opcao == "0":
        print("Encerrando...")
        break
    else:
        print("Opção inválida.")
