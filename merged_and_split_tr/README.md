# Split / Merge de Arquivos de Tandem Repeats

Dois scripts complementares, `split.py` e `merge.py`, para **dividir** e
**remontar** arquivos de texto contendo dados de *Tandem Repeats*, organizados
por espécie.

## Requisitos

- Python 3 (utiliza apenas a biblioteca padrão: `os`, `re`, `shutil`)

---

## 1. `split.py` — Divisão de Arquivos

### Funcionalidade

Lê cada arquivo `.txt` da pasta de entrada `files_tr/`, divide o conteúdo pelos
cabeçalhos `>` e grava **um arquivo por bloco** em uma subpasta nomeada conforme
o arquivo de origem, dentro de `separated/`.

### Como Usar

Execute **a partir de dentro** da pasta `merged_and_split_tr/` (os caminhos
`files_tr/` e `separated/` são relativos ao diretório de trabalho):

```sh
cd merged_and_split_tr
python3 split.py
```

Resultado: `separated/<nome_do_arquivo>/<bloco>.txt`.

---

## 2. `merge.py` — Mesclagem de Arquivos

### Funcionalidade

Percorre as subpastas em `separeted/` e mescla todos os `.txt` de cada subpasta
em um único arquivo dentro de `merged/`, nomeado conforme a subpasta. Os arquivos
são ordenados pelo nome após o primeiro `_`. Se houver apenas arquivos soltos
(em vez de subpastas), eles são mesclados em um único `merged.txt`.

### Como Usar

Execute **a partir da raiz do repositório** (os caminhos em `merge.py` são
relativos à raiz):

```sh
python3 merged_and_split_tr/merge.py
```

Resultado: `merged_and_split_tr/merged/<subpasta>.txt`.

## Observações

- **Atenção aos nomes/locais das pastas**: o `split.py` grava em `separated/`
  (relativo ao diretório onde é executado), enquanto o `merge.py` lê de
  `merged_and_split_tr/separeted/` (note a grafia diferente, relativa à raiz do
  repositório). Ao encadear os dois scripts, garanta que a saída do `split.py`
  esteja no diretório que o `merge.py` espera ler.
- As pastas `files_tr/`, `separated/` e `merged/` não são versionadas
  (ver `.gitignore`).

## Autor

Julio-CSilva
