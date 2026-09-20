import random
from cliente import Cliente
from fila_classica import Fila
from fila_circular import FilaCircular
from fila_prioridade import FilaPrioridade


def gerar_clientes(quantidade):
    clientes = []
    for i in range(1, quantidade + 1):
        nome = f"Cliente {i}"
        senha = f"S{i:03}"
        prioridade = random.randint(1, 3)
        clientes.append(Cliente(nome, senha, prioridade))
    return clientes


def demonstrar():
    print("\n=== DESAFIO FINAL - SIMULAÇÃO COM 20 CLIENTES ===")
    clientes = gerar_clientes(20)

    print("\nClientes na ordem de chegada:")
    for cliente in clientes:
        print(f"  {cliente}")

    # --- Fila Clássica ---
    print("\n--- Fila Clássica: ordem de atendimento ---")
    fila_classica = Fila()
    for cliente in clientes:
        fila_classica.enqueue(cliente)
    ordem_classica = []
    while not fila_classica.empty():
        ordem_classica.append(fila_classica.dequeue())
    for cliente in ordem_classica:
        print(f"  {cliente}")

    # --- Fila Circular ---
    print("\n--- Fila Circular (capacidade 5): comportamento ---")
    fila_circular = FilaCircular(capacidade=5)
    ordem_circular = []
    for cliente in clientes:
        if fila_circular.full():
            ordem_circular.append(fila_circular.dequeue())
        fila_circular.enqueue(cliente)
    while not fila_circular.empty():
        ordem_circular.append(fila_circular.dequeue())

    # --- Fila de Prioridade ---
    print("\n--- Fila de Prioridade: ordem de atendimento ---")
    fila_prioridade = FilaPrioridade()
    for cliente in clientes:
        fila_prioridade.enqueue(cliente)
    ordem_prioridade = []
    while not fila_prioridade.empty():
        atendido = fila_prioridade.dequeue()
        ordem_prioridade.append(atendido)
        print(f"  {atendido}")

    # --- Comparação ---
    print("\n=== COMPARAÇÃO DOS RESULTADOS ===")
    print(f"{'Posição':<8} | {'Clássica':<15} | {'Circular':<15} | {'Prioridade':<15}")
    for i in range(20):
        print(f"{i + 1:<8} | {ordem_classica[i].nome:<15} | "
              f"{ordem_circular[i].nome:<15} | {ordem_prioridade[i].nome:<15}")

    mesma_classica_circular = [c.nome for c in ordem_classica] == [c.nome for c in ordem_circular]
    mesma_classica_prioridade = [c.nome for c in ordem_classica] == [c.nome for c in ordem_prioridade]
    print(f"\nFila Clássica e Fila Circular produziram a mesma ordem? {mesma_classica_circular}")
    print(f"Fila Clássica e Fila de Prioridade produziram a mesma ordem? {mesma_classica_prioridade}")


if __name__ == "__main__":
    demonstrar()
