


#Criando uma pilha
pilha = []

#Inserindo elementos (push)
pilha.append(10)
pilha.append(20)
pilha.append(30)
pilha.append(40)
print("Pilh atual: ", pilha)

#Removendo elemento (pop)
elemento = pilha.pop()
print("Elemento removido: ", elemento)
print("Pilha atual: ", pilha)
#Consultando o topo (peek)
topo = pilha[-1]
print("Elemento do topo: ", topo)
#Verificando se está vazia
print("Pilha vazia? ", len(pilha) == 0)