# Estrutura de Dados II

Repositório com os algoritmos e atividades da disciplina.

## Estrutura do repositório

```
Algoritmos/            -> Implementações de referência de cada algoritmo
                           estudado na disciplina, uma pasta por algoritmo.
                           Vai crescendo ao longo do semestre.
    BubbleSort/
    QuickSort/

Parte1_Pesquisa/        -> Pesquisa comparativa Bubble Sort x Quick Sort
Parte2_Ordenacao/       -> Experimento prático de ordenação
Parte3_BuscaMatriz/     -> Busca sequencial em matrizes
Parte4_HandsOn1/        -> Array de temperaturas
Parte5_HandsOn2/        -> Matriz de sensores
Parte6_Conclusao/       -> Análise e conclusão final

main.py                 -> Ponto de entrada único da atividade, com um
                           menu para rodar cada parte
```

## Sobre a organização em pastas + main.py

Cada parte da atividade fica na sua própria pasta (`Parte2_Ordenacao/`,
`Parte3_BuscaMatriz/`, etc), isolada das demais — isso facilita achar e
avaliar cada critério separadamente.

Mesmo assim, o `main.py` na raiz funciona como um ponto de entrada único:
ele reúne as partes e permite executar qualquer uma delas a partir de um
só lugar, sem precisar entrar em cada pasta manualmente. Ele não junta o
código das partes num arquivo só — cada uma continua rodando como um
programa independente, mas todas acessíveis pelo mesmo menu.

## Como rodar

A forma recomendada é pelo `main.py`, na raiz do repositório:

```
python main.py
```

Ele mostra um menu para escolher qual parte executar (Parte 2 a 5) e
continua rodando até você escolher sair.

Também é possível rodar cada parte individualmente:

```
python Parte2_Ordenacao/parte2.py
```

## Atividade: Arrays, Matrizes, Ordenação e Busca (29/08)

Atividade avaliativa envolvendo Bubble Sort, Quick Sort, busca
sequencial em matrizes e manipulação de arrays/matrizes aplicados a
cenários práticos (temperaturas e sensores).
