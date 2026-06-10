# Organização de Arquivos por Lista (move_file.py)

Script para organizar arquivos em pastas com base em uma lista de espécies
agrupadas. Lê um arquivo de texto com grupos separados por `----` e move os
arquivos correspondentes para subpastas numeradas (`div_1`, `div_2`, ...).

## Como Funciona

1. Lê o arquivo de lista (`sort.txt`), separando os nomes em grupos pelos
   delimitadores `----`.
2. Para cada grupo, cria uma pasta `results/div_N`.
3. Move, do diretório de origem para a pasta do grupo, todo arquivo cujo nome
   contenha o nome da espécie. A comparação ignora maiúsculas/minúsculas e troca
   espaços por `_`.

## Requisitos

- Python 3 (utiliza apenas a biblioteca padrão: `os`, `shutil`, `pathlib`)

## Como Usar

Os caminhos no script são relativos à **raiz do repositório**, então execute a
partir dela. Ajuste, se necessário, as variáveis no início do script:

```python
dir_origem = "mv_file/files"      # Diretório dos arquivos a organizar
list_species = "mv_file/sort.txt" # Lista de espécies com divisores "----"
```

Formato do `sort.txt`:

```text
Especie A
Especie B
----
Especie C
Especie D
```

Execução:

```sh
python3 mv_file/move_file.py
```

## Resultado

Os arquivos correspondentes são movidos para `mv_file/results/div_N`, conforme
os grupos definidos no `sort.txt`. Arquivos sem correspondência permanecem no
diretório de origem.

## Observações

- A operação **move** os arquivos (não copia).
- As pastas `files/` e `results/` não são versionadas (ver `.gitignore`).

## Autor

Julio-CSilva
