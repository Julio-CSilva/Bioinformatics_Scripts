# Extração de Contigs dos Arquivos FASTA

O script `ext_gen.py` extrai genes específicos de arquivos `.fasta`/`.fa` e salva os resultados em arquivos separados no formato FASTA.

## Requisitos

Para executar o script, é necessário ter o Python instalado e garantir que os arquivos `.fasta` ou `.fa` estejam disponíveis no diretório correto.

## Como Usar

1. **Defina o diretório dos arquivos FASTA**:
   ```python
   dir_fasta = "fastas"
   ```
2. **Defina o(s) Contig(s) que será(ão) extraído(s)**:
   ```python
   gen = ["COXI", "SRR86212594", "contig1_osteoglossum"]
   ```
   *Se a lista estiver vazia (`gen = []`), todos os contigs serão extraídos.*

3. **Defina o diretório onde os arquivos extraídos serão salvos**:
   ```python
   dir_resultados = "results"
   ```

4. **Execute o script**:
   ```sh
   python3 ext_gen.py
   ```

## Estrutura do Arquivo de Saída

Os arquivos extraídos serão salvos no diretório definido em `dir_resultados`, com nomes no formato:

```
<NOME_DO_ARQUIVO>_<NOME_DO_CONTIG>.fasta
```

Exemplo:
```
sample_COXI.fasta
sample_COXII.fasta
```

## Exemplo de Uso

Se tivermos um arquivo `sequencias.fasta` com os seguintes contigs:
```
>COXI
ATGCGTACGATCGTACG
>COXII
TGCATGCTAGCTAGCTA
>COXIII
CGTAGCTAGCTAGTACG
```
E definirmos `gen = ["COXI", "COXIII"]`, os arquivos gerados serão:
```
results/sequencias_COXI.fasta
results/sequencias_COXIII.fasta
```

## Autor
Este script foi desenvolvido para facilitar a extração de genes em análises bioinformáticas.

