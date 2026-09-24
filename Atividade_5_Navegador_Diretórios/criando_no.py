from class_no.no import No

# Criando nós
sistema = No("Sistema")
documentos = No("Documentos")
projetos = No("Projetos")
textos = No("Textos")
planilhas = No("Planilhas")
python = No("Python")
java = No("Java")

# Conectar formando a árvore
sistema.esquerda = documentos
sistema.direita = projetos

documentos.esquerda = textos
documentos.direita = planilhas

projetos.esquerda = python
projetos.direita = java

def pre_ordem(no, resultado=None):
    if resultado is None:
        resultado = []
    if no:
        resultado.append(no.valor)         # Nó
        pre_ordem(no.esquerda, resultado)  # Esquerda
        pre_ordem(no.direita, resultado)   # Direita
    return resultado


def em_ordem(no, resultado=None):
    if resultado is None:
        resultado = []
    if no:
        em_ordem(no.esquerda, resultado)   # Esquerda
        resultado.append(no.valor)         # Nó
        em_ordem(no.direita, resultado)    # Direita
    return resultado


def pos_ordem(no, resultado=None):
    if resultado is None:
        resultado = []
    if no:
        pos_ordem(no.esquerda, resultado)  # Esquerda
        pos_ordem(no.direita, resultado)   # Direita
        resultado.append(no.valor)         # Nó
    return resultado


# Mostrar no terminal
print("Pré-ordem:", pre_ordem(sistema))
print("Em-ordem: ", em_ordem(sistema))
print("Pós-ordem:", pos_ordem(sistema))
