# Sistema Inteligente de Atendimento com Filas

Simulação de uma central de atendimento usando três estruturas de fila:
Fila Clássica (FIFO), Fila Circular e Fila de Prioridade.

## Como rodar

```bash
python Atendimento_com_Filas/atividade_4.py
```

## Estrutura

```text
Atendimento_com_Filas/
    cliente.py           -> Classe Cliente (nome, senha, prioridade)
    fila_classica.py      -> Parte 1: Fila FIFO clássica
    fila_circular.py      -> Parte 2: Fila Circular (capacidade fixa)
    fila_prioridade.py    -> Parte 3: Fila de Prioridade (heapq)
    desafio_final.py      -> Desafio Final: simulação com 20 clientes
    atividade_4.py         -> Arquivo principal, importa e roda as 4 partes
```

- **Parte 1** (`fila_classica.py`): `Fila` — FIFO clássica, com `enqueue`, `dequeue`, `head`, `size`, `empty`.
- **Parte 2** (`fila_circular.py`): `FilaCircular` — capacidade fixa (5), reaproveita posições liberadas via aritmética modular (`% capacidade`).
- **Parte 3** (`fila_prioridade.py`): `FilaPrioridade` — usa `heapq`, com tuplas `(prioridade, contador, cliente)` para garantir desempate por ordem de chegada.
- **Desafio Final** (`desafio_final.py`): gera 20 clientes aleatórios e compara o resultado das três estruturas.

Cada arquivo pode ser executado individualmente (ex: `python fila_circular.py`) para testar só aquela parte, ou todos juntos via `atividade_4.py`.

## Relatório e Análise

**1) Por que a ordem de atendimento da fila de prioridade pode ser diferente da ordem da fila clássica?**

A fila clássica atende estritamente na ordem de chegada (FIFO), sem olhar
para nenhum outro critério. Já a fila de prioridade reorganiza os
clientes com base no valor de prioridade (1 = Emergência primeiro),
independente de quando cada um chegou. Um cliente que chegou por último,
mas com prioridade 1, é atendido antes de quem chegou primeiro com
prioridade 3. A ordem só coincide com a da fila clássica no caso
degenerado em que todos os clientes têm a mesma prioridade.

**2) Em quais situações reais uma fila de prioridade seria mais adequada?**

Em qualquer cenário onde a urgência importa mais do que a ordem de
chegada: pronto-socorro hospitalar (emergências primeiro), sistemas
operacionais escalonando processos críticos, filas de suporte técnico
com clientes com contrato premium, ou sistemas de resgate/segurança
pública, onde atender por ordem de chegada poderia custar vidas ou
causar prejuízos maiores.

**3) Quais são as vantagens e limitações de uma fila circular?**

*Vantagens*: usa um espaço de memória fixo e reaproveita posições
liberadas, evitando o desperdício de memória que uma fila linear (baseada
em lista, com `pop(0)`) teria ao deslocar todos os elementos a cada
remoção. As operações de inserção e remoção são O(1).

*Limitações*: tem capacidade fixa, definida na criação — não cresce
sozinha. Se a demanda ultrapassar a capacidade, novos elementos são
recusados até que haja espaço liberado por uma remoção. Exige controle
cuidadoso dos índices `front` e `rear` (com aritmética modular) para não
confundir fila cheia com fila vazia, já que os dois casos podem ter
`front == rear` dependendo da implementação.

**4) O que acontece ao tentar inserir um elemento em uma fila circular cheia?**

Na implementação feita aqui, o método `enqueue` verifica `full()` antes
de inserir; se a fila já estiver na capacidade máxima, a inserção é
recusada (retorna `False` e imprime um aviso), sem sobrescrever nenhum
dado existente. Só é possível inserir um novo cliente depois que algum
`dequeue()` libera uma posição.
