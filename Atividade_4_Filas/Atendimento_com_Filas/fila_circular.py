from cliente import Cliente


class FilaCircular:
    def __init__(self, capacidade=5):
        self.capacidade = capacidade
        self._itens = [None] * capacidade
        self.front = 0
        self.rear = -1
        self.quantidade = 0

    def empty(self):
        return self.quantidade == 0

    def full(self):
        return self.quantidade == self.capacidade

    def enqueue(self, cliente):
        if self.full():
            print(f"  [CHEIA] Não foi possível inserir {cliente.nome} - fila circular cheia.")
            return False
        self.rear = (self.rear + 1) % self.capacidade
        self._itens[self.rear] = cliente
        self.quantidade += 1
        print(f"  Inserido: {cliente.nome} | front={self.front} rear={self.rear}")
        return True

    def dequeue(self):
        if self.empty():
            return None
        cliente = self._itens[self.front]
        self._itens[self.front] = None
        self.front = (self.front + 1) % self.capacidade
        self.quantidade -= 1
        print(f"  Removido: {cliente.nome} | front={self.front} rear={self.rear}")
        return cliente


def demonstrar():
    print("\n=== PARTE 2 - FILA CIRCULAR (capacidade 5) ===")
    fila = FilaCircular(capacidade=5)
    clientes = [Cliente(f"Cliente {i}", f"S{i:03}", 1) for i in range(1, 8)]

    print("Preenchendo a fila até a capacidade:")
    for cliente in clientes[:5]:
        fila.enqueue(cliente)

    print("\nTentando inserir com a fila cheia:")
    fila.enqueue(clientes[5])

    print("\nRemovendo um cliente para liberar posição:")
    fila.dequeue()

    print("\nInserindo novo cliente - reaproveitando a posição liberada:")
    fila.enqueue(clientes[6])

    print("\nEsvaziando a fila:")
    while not fila.empty():
        fila.dequeue()


if __name__ == "__main__":
    demonstrar()
