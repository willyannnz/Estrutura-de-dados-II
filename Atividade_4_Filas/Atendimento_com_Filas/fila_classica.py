import random
from cliente import Cliente


class Fila:
    def __init__(self):
        self._itens = []

    def enqueue(self, cliente):
        self._itens.append(cliente)

    def dequeue(self):
        if self.empty():
            return None
        return self._itens.pop(0)

    def head(self):
        if self.empty():
            return None
        return self._itens[0]

    def size(self):
        return len(self._itens)

    def empty(self):
        return len(self._itens) == 0


def demonstrar():
    print("\n=== PARTE 1 - FILA CLÁSSICA (FIFO) ===")
    fila = Fila()

    clientes = [Cliente(f"Cliente {i}", f"S{i:03}", random.randint(1, 3)) for i in range(1, 11)]

    print("Ordem de chegada (cadastro):")
    for cliente in clientes:
        fila.enqueue(cliente)
        print(f"  Entrou: {cliente}")

    print(f"\nTamanho da fila: {fila.size()}")
    print(f"Próximo a ser atendido (head): {fila.head()}")

    print("\nOrdem de atendimento (dequeue):")
    ordem_atendimento = []
    while not fila.empty():
        atendido = fila.dequeue()
        ordem_atendimento.append(atendido)
        print(f"  Atendido: {atendido}")

    nomes_chegada = [c.nome for c in clientes]
    nomes_atendimento = [c.nome for c in ordem_atendimento]
    print(f"\nOrdem de chegada == ordem de atendimento? {nomes_chegada == nomes_atendimento}")


if __name__ == "__main__":
    demonstrar()
