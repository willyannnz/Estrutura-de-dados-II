import heapq
import random


class Cliente:
    def __init__(self, nome, senha, prioridade):
        self.nome = nome
        self.senha = senha
        self.prioridade = prioridade

    def __repr__(self):
        return f"{self.nome} (senha {self.senha}, prioridade {self.prioridade})"


# ============================================================
# PARTE 1 - FILA CLÁSSICA (FIFO)
# ============================================================
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


def demonstrar_fila_classica():
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


# ============================================================
# PARTE 2 - FILA CIRCULAR
# ============================================================
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


def demonstrar_fila_circular():
    print("\n=== PARTE 2 - FILA CIRCULAR (capacidade 5) ===")
    fila = FilaCircular(capacidade=5)
    clientes = [Cliente(f"Cliente {i}", f"S{i:03}", random.randint(1, 3)) for i in range(1, 8)]

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


# ============================================================
# PARTE 3 - FILA DE PRIORIDADE (heapq)
# ============================================================
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


def demonstrar_fila_prioridade():
    print("\n=== PARTE 3 - FILA DE PRIORIDADE ===")
    fila = FilaPrioridade()

    # Propositalmente fora de ordem, para provar que a prioridade reorganiza o atendimento
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


# ============================================================
# DESAFIO FINAL - SIMULAÇÃO COMPARATIVA COM 20 CLIENTES
# ============================================================
def gerar_clientes(quantidade):
    clientes = []
    for i in range(1, quantidade + 1):
        nome = f"Cliente {i}"
        senha = f"S{i:03}"
        prioridade = random.randint(1, 3)
        clientes.append(Cliente(nome, senha, prioridade))
    return clientes


def desafio_final():
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
        nome_classica = ordem_classica[i].nome
        nome_circular = ordem_circular[i].nome
        nome_prioridade = ordem_prioridade[i].nome
        print(f"{i + 1:<8} | {nome_classica:<15} | {nome_circular:<15} | {nome_prioridade:<15}")

    mesma_ordem_classica_circular = [c.nome for c in ordem_classica] == [c.nome for c in ordem_circular]
    mesma_ordem_classica_prioridade = [c.nome for c in ordem_classica] == [c.nome for c in ordem_prioridade]
    print(f"\nFila Clássica e Fila Circular produziram a mesma ordem? {mesma_ordem_classica_circular}")
    print(f"Fila Clássica e Fila de Prioridade produziram a mesma ordem? {mesma_ordem_classica_prioridade}")


def main():
    demonstrar_fila_classica()
    demonstrar_fila_circular()
    demonstrar_fila_prioridade()
    desafio_final()


if __name__ == "__main__":
    main()
