# Extração de Contigs dos Arquivos FASTA

O script `ext_gen.py` extrai genes específicos de arquivos `.fasta`/`.fa` e salva os resultados em arquivos separados no formato FASTA.

## Requisitos

- Python 3 (utiliza apenas a biblioteca padrão: `os`)
- Arquivos `.fasta`/`.fa` no diretório de entrada.

## Como Usar

As configurações ficam no início do script. Por padrão os caminhos são
relativos à **raiz do repositório**, então execute o script a partir dela.

1. **Defina o diretório dos arquivos FASTA**:
   ```python
   dir_fasta = "extrator_genes/fastas"
   ```
2. **Defina o(s) Contig(s) que será(ão) extraído(s)**:
   ```python
   gen = ["COXI", "SRR86212594", "contig1_osteoglossum"]
   ```
   *Se a lista estiver vazia (`gen = []`), todos os contigs serão extraídos.*

3. **Defina o diretório onde os arquivos extraídos serão salvos**:
   ```python
   dir_resultados = "extrator_genes/results"
   ```

4. **Execute o script** (a partir da raiz do repositório):
   ```sh
   python3 extrator_genes/ext_gen.py
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

Julio-CSilva

