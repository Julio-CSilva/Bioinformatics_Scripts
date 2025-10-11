# Atualização e Renomeação de Arquivos FASTA

Este projeto contém um script, `main.py`, desenvolvido para padronizar nomes de arquivos `.fasta`/`.fa` e atualizar seus cabeçalhos com base em um dicionário de espécies.

## 1. rename_fasta.py - Renomeação e Atualização de Cabeçalhos

### Funcionalidade
O script `main.py` realiza a leitura de arquivos FASTA localizados em um diretório e atualiza o primeiro `CONTIG` de cada arquivo com um novo identificador no formato `>sigla_Especie`, com base em um dicionário fornecido (`dict_species_orderby.txt`).  
Além disso, renomeia o arquivo utilizando o mesmo padrão, resultando em arquivos como `sigla_Especie.fa`.

### Como Usar
1. Coloque os arquivos `.fasta` ou `.fa` na pasta definida em `dir_path`.
2. Crie um arquivo `dict_species_orderby.txt` no formato:
3. Execute o script `main.py`.

### Exemplo de Entrada
**Arquivo:** `ABCD_contigs.fa`  
**Conteúdo original:**
```fasta
>contig1
ATCGATCGATCG

```

**Resultado:**
```fasta
>ABCD_EspecieAlpha
ATCGATCGATCG
```
