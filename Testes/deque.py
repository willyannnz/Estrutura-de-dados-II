from collections import deque
fila = deque()
print("Fila Vazia? ", len(fila) == 0) #True
fila.append("Ana") #enqueue
fila.append("João") #enqueue
fila.append("Maria") #enqueue
print("Fila atual: ", list(fila))
print("Primeiro da fila (peek): ", fila[0])
atendido = fila.popleft() #dequeue
print("Atendido: ", atendido)
print("Fila depois: ", list(fila))
print("Lista Vazia?" , len(fila) == 0)
