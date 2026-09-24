# 📚 Estrutura de Dados II — Atividades Práticas

Repositório destinado às atividades práticas e hands-on da disciplina de **Estrutura de Dados II** (UDF).

---

## 📁 Estrutura do Repositório

```text
Estrutura-de-dados-II/
│
├── Atividade_5/
│   ├── class_no/
│   │   └── no.py
│   ├── Navegador_Diretórios/
│   │   └── navegador.py
│   └── Priorizacao_Chamados/
│       └── chamados.py
│
└── README.md
```

---

## 🚀 Conteúdo das Atividades

### 🔹 Atividade 5 — Hands-on 1: Navegador de Diretórios
Representação de uma estrutura de pastas como árvore binária, com implementação dos três percursos clássicos: pré-ordem, em-ordem e pós-ordem.

#### 🌳 Estrutura da Árvore
```text
             Sistema
            /       \
       Documentos     Projetos
        /     \       /      \
     Textos  Planilhas Python  Java
```

#### 📄 Arquivos
* `Atividade_5/class_no/no.py` — classe `No`, com os atributos `valor`, `esquerda` e `direita`.
* `Atividade_5/Navegador_Diretórios/navegador.py` — monta a árvore e executa os três percursos.

#### ▶️ Como Executar
```bash
python -m Atividade_5.Navegador_Diretórios.navegador
```

#### 🖥️ Resultado Esperado
```text
Pré-ordem: ['Sistema', 'Documentos', 'Textos', 'Planilhas', 'Projetos', 'Python', 'Java']
Em-ordem:  ['Textos', 'Documentos', 'Planilhas', 'Sistema', 'Python', 'Projetos', 'Java']
Pós-ordem: ['Textos', 'Planilhas', 'Documentos', 'Python', 'Java', 'Projetos', 'Sistema']
```

#### 📚 Quando Usar Cada Percurso
* **Pré-ordem** (Nó → Esquerda → Direita): útil para copiar ou recriar a estrutura da árvore, pois o pai é visitado antes dos filhos. Também pode ser usada para serializar a árvore e salvar sua estrutura em um arquivo.
* **Em-ordem** (Esquerda → Nó → Direita): em uma árvore de busca binária (BST), devolve os valores em ordem crescente. Nesta árvore de diretórios, que não está ordenada, o resultado não possui esse significado, mas representa o percurso clássico de referência.
* **Pós-ordem** (Esquerda → Direita → Nó): útil quando os filhos precisam ser processados antes do pai, como ao calcular o tamanho total de uma pasta ou excluir a árvore sem perder as referências dos nós filhos.

---

### 🔹 Atividade 5 — Hands-on 2: Priorização de Chamados
* **Objetivo:** Organizar chamados técnicos baseados em código de prioridade utilizando uma Árvore Binária não balanceada.
* **Localização:** `Atividade_5/Priorizacao_Chamados/chamados.py`

#### 🌲 Estrutura da Árvore Representada
```text
          50
        /    \
      30      70
     /          \
    20          90
      \        /
      25      80
```

#### 📋 Percursos na Árvore
* **Pré-Ordem** (*Raiz $\rightarrow$ Esquerda $\rightarrow$ Direita*): `[50, 30, 20, 25, 70, 90, 80]`
* **Em-Ordem** (*Esquerda $\rightarrow$ Raiz $\rightarrow$ Direita*): `[20, 25, 30, 50, 70, 80, 90]`
* **Pós-Ordem** (*Esquerda $\rightarrow$ Direita $\rightarrow$ Raiz*): `[25, 20, 30, 80, 90, 70, 50]`

---

## 📝 Respostas da Análise (Hands-on 2)

1. **Qual percurso visita a prioridade 50 primeiro?**
   * **Resposta:** O percurso **Pré-ordem**. Por definição, a pré-ordem processa a raiz antes de visitar os subárvores esquerda e direita.

2. **Em qual percurso a prioridade 50 aparece por último?**
   * **Resposta:** O percurso **Pós-ordem**. A pós-ordem visita completamente as subárvores esquerda e direita antes de processar o nó raiz.

3. **Como os filhos ausentes são tratados pelo algoritmo?**
   * **Resposta:** Os ponteiros/referências para filhos ausentes contêm o valor `None`. Nas funções recursivas de travessia, a condição de parada `if no is not None:` verifica se o nó existe; caso seja `None`, a recursão atinge o caso base e retorna imediatamente sem processar nem adicionar valores à lista.

---

## 💻 Como Executar

Certifique-se de ter o **Python 3** instalado em sua máquina.

> ⚠️ **Importante:** os scripts usam import relativo (`from ..class_no.no import No`) para acessar a classe `No` compartilhada. Por isso, **não rode os arquivos `.py` diretamente** (nem pelo botão ▶️ Run do VS Code) — isso gera `ImportError: attempted relative import with no known parent package`. Sempre rode com `python -m`, a partir da pasta raiz do repositório (`Estrutura-de-dados-II/`), como nos comandos abaixo.

1. Clone o repositório:
   ```bash
   git clone https://github.com/willyannnz/Estrutura-de-dados-II.git
   cd Estrutura-de-dados-II
   ```

2. Executar o Hands-on 1 (Navegador de Diretórios):
   ```bash
   python -m Atividade_5.Navegador_Diretórios.navegador
   ```

3. Executar o Hands-on 2 (Priorização de Chamados):
   ```bash
   python -m Atividade_5.Priorizacao_Chamados.chamados
   ```

---

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.x
* **Conceitos:** Árvores Binárias de Busca (BST), Percursos Recursivos (Pré-ordem, Em-ordem, Pós-ordem).