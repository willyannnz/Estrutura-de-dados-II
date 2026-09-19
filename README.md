# Estrutura de Dados II

Repositório com os algoritmos e atividades da disciplina.

## Estrutura do repositório

```text
Algoritmos/                       -> Implementações de referência de cada algoritmo
                                    estudado na disciplina, uma pasta por algoritmo.
                                    Vai crescendo ao longo do semestre.
    BubbleSort/
    QuickSort/
    InsertionSort/
    SelectionSort/

Atividade_2_ArraysMatrizes/       -> Arrays, matrizes, ordenação e busca
    Parte1_Pesquisa/              -> Pesquisa comparativa Bubble Sort x Quick Sort
    Parte2_Ordenacao/             -> Experimento prático de ordenação
    Parte3_BuscaMatriz/           -> Busca sequencial em matrizes
    Parte4_HandsOn1/              -> Array de temperaturas
    Parte5_HandsOn2/              -> Matriz de sensores
    Parte6_Conclusao/             -> Análise e conclusão final

Atividade_3_Ordenacao/            -> Central de distribuição de pedidos
    experimento_ordenacao.py      -> Bubble, Insertion, Selection e Quick Sort,
                                    testados com vetores de 10, 20 e 1.000
    desafio_adicional.py          -> Mesmos 4 algoritmos comparados em vetor
                                    aleatório, já ordenado e em ordem inversa

Atividade_4_Filas/                -> Sistema Inteligente de Atendimento com Filas
                                    (em andamento)

main.py                           -> Ponto de entrada único das atividades, com
                                    um menu para rodar cada parte/experimento

README.md                         -> Documentação e apresentação do projeto
```

## Sobre a organização em pastas + main.py

Cada atividade fica na sua própria pasta (`Atividade_2_ArraysMatrizes/`, `Atividade_3_Ordenacao/`, ...), e dentro dela cada parte/experimento também tem sua própria subpasta ou arquivo — isso facilita achar e avaliar cada critério separadamente.

Mesmo assim, o `main.py` na raiz funciona como um ponto de entrada único: ele reúne as partes e permite executar qualquer uma delas a partir de um só lugar, sem precisar entrar em cada pasta manualmente. Ele não junta o código das partes num arquivo só — cada uma continua rodando como um programa independente, mas todas acessíveis pelo mesmo menu.

## Como rodar

A forma recomendada é pelo `main.py`, na raiz do repositório:

```bash
python main.py
```

Ele mostra um menu com as opções da Atividade 2 (1 a 4) e da Atividade 3 (5 e 6), e continua rodando até você escolher sair.

Também é possível rodar cada script individualmente:

```bash
python "Atividade_2_ArraysMatrizes/Parte2_Ordenacao/parte2.py"
python "Atividade_2_ArraysMatrizes/Parte3_BuscaMatriz/parte3.py"
python "Atividade_2_ArraysMatrizes/Parte4_HandsOn1/parte4.py"
python "Atividade_2_ArraysMatrizes/Parte5_HandsOn2/parte5.py"
python "Atividade_3_Ordenacao/experimento_ordenacao.py"
python "Atividade_3_Ordenacao/desafio_adicional.py"
```

## Atividade 2: Arrays, Matrizes, Ordenação e Busca (29/08)

Atividade avaliativa envolvendo Bubble Sort, Quick Sort, busca sequencial em matrizes e manipulação de arrays/matrizes aplicados a cenários práticos (temperaturas e sensores).

## Atividade 3: Central de Distribuição de Pedidos

Atividade avaliativa comparando quatro algoritmos de ordenação (Bubble, Insertion, Selection e Quick Sort) quanto ao número de comparações e trocas/movimentações, em vetores de 10, 20 e 1.000 elementos. Inclui desafio adicional analisando o efeito da organização inicial dos dados (aleatório, ordenado, invertido) no desempenho de cada algoritmo.

## Atividade 4: Sistema Inteligente de Atendimento com Filas

Atividade avaliativa envolvendo a estrutura de dados fila (queue). Em andamento.
