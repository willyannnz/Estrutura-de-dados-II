import heapq
from cliente import Cliente


class FilaPrioridade:
    def __init__(self):
        self._heap = []
        self._contador = 0

    def enqueue(self, cliente):
        # (prioridade, contador, cliente) -> contador garante desempate por ordem de chegada
        heapq.heappush(self._heap, (cliente.prioridade, self._contador, cliente))
        self._contador += 1

    def dequeue(self):
        if self.empty():
            return None
        _, _, cliente = heapq.heappop(self._heap)
        return cliente

    def size(self):
        return len(self._heap)

    def empty(self):
        return len(self._heap) == 0


def demonstrar():
    print("\n=== PARTE 3 - FILA DE PRIORIDADE ===")
    fila = FilaPrioridade()

    dados = [
        ("Cliente A", 3), ("Cliente B", 1), ("Cliente C", 2),
        ("Cliente D", 1), ("Cliente E", 3), ("Cliente F", 2),
    ]

    print("Ordem de chegada:")
    for nome, prioridade in dados:
        cliente = Cliente(nome, f"S-{nome[-1]}", prioridade)
        fila.enqueue(cliente)
        print(f"  Entrou: {cliente}")

    print("\nOrdem de atendimento (prioridade primeiro, chegada como desempate):")
    while not fila.empty():
        print(f"  Atendido: {fila.dequeue()}")


if __name__ == "__main__":
    demonstrar()
