from collections import deque

fila = deque([10,20,30,40,50])

#Usando head (peek)
proximo = fila[0]
print("Elemento no inicio (head): ", proximo)

#Usando size
quantidade = len(fila)
print("Quantidade de elementos (size): ", quantidade)