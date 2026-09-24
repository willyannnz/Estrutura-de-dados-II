# ⚠️ Import relativo ("..class_no") — não dá pra rodar este arquivo direto (nem no ▶️ Run do VS Code).
# Rode como módulo, a partir da raiz do repo (pasta Estrutura-de-dados-II):
#   python -m Atividade_5.Priorizacao_Chamados.chamados

from ..class_no.no import No

# Criando nós (prioridades dos chamados)
no_50 = No(50)
no_30 = No(30)
no_70 = No(70)
no_20 = No(20)
no_90 = No(90)
no_25 = No(25)
no_80 = No(80)

# Conectar formando a árvore
no_50.esquerda = no_30
no_50.direita = no_70

no_30.esquerda = no_20
no_20.direita = no_25

no_70.direita = no_90
no_90.esquerda = no_80


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


# Obter os resultados dos percursos
lista_pre = pre_ordem(no_50)
lista_em = em_ordem(no_50)
lista_pos = pos_ordem(no_50)

# Mostrar no terminal
print("Pré-ordem:", lista_pre)
print("Em-ordem: ", lista_em)
print("Pós-ordem:", lista_pos)

# Verificação se a saída Em-ordem está crescente
print("Em-ordem está crescente?", lista_em == sorted(lista_em))