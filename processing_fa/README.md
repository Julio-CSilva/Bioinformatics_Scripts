# Processamento de Arquivos FASTA (rename_fasta.py)

Script para padronizar arquivos FASTA mantendo **apenas a maior contig** de cada
arquivo e reescrevendo o cabeçalho com o nome do próprio arquivo. É útil para
limpar montagens que contêm contigs secundárias, deixando cada FASTA com uma
única sequência (a maior) e um cabeçalho consistente.

## Como Funciona

Para cada arquivo dentro da pasta `fasta/`:

1. Lê todas as contigs do arquivo.
2. Seleciona a **maior contig** (pelo número de bases).
3. Substitui o cabeçalho por `>` + o nome do arquivo **sem a extensão**.
4. **Sobrescreve o arquivo no lugar**, mantendo apenas o novo cabeçalho e a
   maior sequência. (O nome físico do arquivo **não** é alterado.)

Arquivos vazios ou inválidos são ignorados, e subdiretórios são pulados.

## Requisitos

- Python 3 (utiliza apenas a biblioteca padrão: `os`)

## Como Usar

1. Coloque os arquivos `.fa`/`.fasta` na pasta `fasta/` (ao lado do script).
   Como o cabeçalho final é derivado do **nome do arquivo**, nomeie os arquivos
   já no padrão desejado, por exemplo `ABCD_EspecieAlpha.fa`.
2. Execute o script:

```sh
python3 rename_fasta.py
```

> O arquivo auxiliar `dict_species_orderby.txt` serve como referência de
> mapeamento espécie → sigla, para ajudar a renomear os arquivos **antes** da
> execução. O script em si lê o cabeçalho a partir do nome do arquivo.

## Exemplo

**Arquivo:** `ABCD_EspecieAlpha.fa`

**Conteúdo original** (várias contigs):

```fasta
>contig1
ATCGATCG
>contig2
ATCGATCGATCGATCGATCGATCG
```

**Resultado** (apenas a maior contig, com novo cabeçalho):

```fasta
>ABCD_EspecieAlpha
ATCGATCGATCGATCGATCGATCG
```

## Observações

- A operação é **destrutiva**: o arquivo original é sobrescrito e as contigs
  menores são descartadas. Faça backup se precisar mantê-las.
- A pasta `fasta/` não é versionada (ver `.gitignore`).

## Autor

Julio-CSilva
