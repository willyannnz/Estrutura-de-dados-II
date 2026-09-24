# Atividade 5 — Navegador de Diretórios (Árvore Binária)

Representação de uma estrutura de pastas como árvore binária, com implementação
dos três percursos clássicos (pré-ordem, em-ordem e pós-ordem).

## Estrutura da árvore

```
                 Sistema
                /       \
         Documentos     Projetos
          /     \       /      \
      Textos  Planilhas Python  Java
```

## Arquivos

- `class_no/no.py` — classe `No`, com os atributos `valor`, `esquerda` e `direita`
- `criando_no.py` — monta a árvore acima e roda os três percursos

## Como rodar

```
python criando_no.py
```

## Resultado esperado

```
Pré-ordem: ['Sistema', 'Documentos', 'Textos', 'Planilhas', 'Projetos', 'Python', 'Java']
Em-ordem:  ['Textos', 'Documentos', 'Planilhas', 'Sistema', 'Python', 'Projetos', 'Java']
Pós-ordem: ['Textos', 'Planilhas', 'Documentos', 'Python', 'Java', 'Projetos', 'Sistema']
```

## Quando usar cada percurso

- **Pré-ordem** (Nó → Esquerda → Direita): útil para *copiar ou recriar* a
  estrutura da árvore, já que o pai é visitado antes dos filhos — por exemplo,
  serializar a árvore para salvar em arquivo.
- **Em-ordem** (Esquerda → Nó → Direita): em uma árvore de busca binária (BST),
  esse percurso devolve os valores em ordem crescente. Aqui a árvore não é
  ordenada, então o resultado não tem esse significado — mas é o percurso
  clássico de referência.
- **Pós-ordem** (Esquerda → Direita → Nó): útil quando é preciso processar os
  filhos antes do pai — por exemplo, calcular o tamanho total de uma pasta
  (soma dos filhos primeiro) ou deletar a árvore inteira sem perder as
  referências dos nós filhos.
