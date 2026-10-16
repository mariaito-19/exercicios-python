# Exercícios de Python

Exercícios acadêmicos de lógica de programação, listas de registros e manipulação de strings.

## Listas de registros

- `ex22NomeFreq.py`: nome da disciplina associada ao registro de menor frequência.
- `ex23medAritAlun.py`: alunos cuja média aritmética corresponde ao valor informado.
- `ex24RAparMediaGeomP.py`: contagem de dígitos pares nos RAs conforme média geométrica ponderada.
- `ex25AlunosReprovados.py`: alunos com ao menos uma nota abaixo de cinco.

São funções para importar e chamar com as listas de entrada; não há menu ou conjunto de dados incluído. O código foi preservado. Há limitações para entradas vazias, alunos sem resultados, pesos nulos e comparações exatas de médias. Não corresponde ao projeto de agenda de contatos.

## Manipulação de strings

- `strings/expansao-intervalos/texto.py`: expande intervalos crescentes entre caracteres, como `a-d` → `abcd`, usando `ord`, `chr`, laços e fatiamento. Mantido conforme enviado, incluindo comentários de aula e demonstração.
- Execute com `python strings/expansao-intervalos/texto.py`. Para experimentar a função, chame `expasao("a-d")`.

Verificação desta inclusão: cinco exemplos conferidos (intervalos de letras e números, intervalo decrescente, texto sem intervalo e string vazia). Isso não representa cobertura de todos os casos possíveis.

## Outros exercícios de listas

- `ex21NomeNota.py`: encontra o nome do aluno associado à maior nota; exige uma lista de resultados não vazia e retorna `None` se não localizar o aluno.
- `freqNome.py`: encontra a matéria com menor frequência em registros no formato `[nome, ..., frequência]`; retorna `None` para lista vazia.
- `ex26DisciplinasSemReprovacao.py`: lista disciplinas sem notas inferiores a cinco. Nesta implementação, disciplinas sem registros também são incluídas. O arquivo foi renomeado para facilitar a leitura, sem alterar a função original.

Foram conferidos seis casos de exemplo destas três funções, incluindo lista vazia em `freqNome`, aluno não localizado e disciplina sem registros. Os arquivos repetidos enviados com `(1)` eram idênticos às versões existentes e não foram duplicados.
