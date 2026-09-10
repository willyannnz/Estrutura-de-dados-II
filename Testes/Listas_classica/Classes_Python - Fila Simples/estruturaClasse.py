class Fila:

    # Inicia uma lista vazia
    def __init__(self):
        self.dados = []

    # Insere um elemento no final
    def enqueue(self, elemento):
        self.dados.append(elemento)

    # Remove o primeiro elemento
    def dequeue(self):
        if not self.empty():
            return self.dados.pop(0)
        return None

    # Retorna o primeiro elemento (sem remover)
    def head(self):
        if not self.empty():
            return self.dados[0]
        return None

    # Retorna o número de elementos
    def size(self):
        return len(self.dados)

    # Verifica se a fila está vazia
    def empty(self):
        return len(self.dados) == 0


# Criando um objeto da classe fila
fila = Fila()

# Inserindo elementos
fila.enqueue("Ana")
fila.enqueue("Bruno")
fila.enqueue("Carla")

print("Primeiro da fila:", fila.head())
print("Tamanho da fila:", fila.size())

# Removendo um elemento
fila.dequeue()

print("Novo primeiro da fila:", fila.head())
print("Novo tamanho da fila:", fila.size())
