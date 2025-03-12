# Análise Estatística de Contigs

O script `analysis_contig.py` realiza a análise Estatísticas de arquivos `.fasta`/`.fa`, coletando informações como:
- **%AT**: Porcentagem de Adenina (A) e Timina (T) na sequência.
- **%CG**: Porcentagem de Citosina (C) e Guanina (G) na sequência.
- **AT Skew**: Métrica que avalia o viés entre Adenina e Timina.

Os resultados são armazenados em um arquivo `.csv`.

## Requisitos

Para executar o script, é necessário ter o Python instalado e garantir que os arquivos `.fasta` ou `.fa` estejam disponíveis no diretório correto.

## Como Usar

1. **Defina o diretório dos arquivos FASTA**:
   ```python
   directory = "dir_files"
   ```
2. **Defina o nome do arquivo de saída**:
   ```python
   output_file = "analysis_contigs.csv"
   ```
3. **Execute o script**:
   ```sh
   python3 analysis_contig.py
   ```

## Estrutura do Arquivo de Saída

O script gera um arquivo `.csv` com as seguintes colunas:

| File | Contigs | Amount | %AT | %CG | AT Skew |
|------|--------|--------|-----|-----|---------|
| Nome do arquivo | Identificação do contig | Quantidade de caracteres | Porcentagem de AT | Porcentagem de CG | Índice AT Skew |

## Exemplo de Saída

```csv
File,Contigs,Amount,%AT,%CG,AT Skew
sample.fasta,>contig_1,1500,55.60,44.40,0.10
sample.fasta,>contig_2,2300,48.75,51.25,-0.05
sample2.fasta,>contig_1,2000,40.30,48.2,-0.02
```

## Autor
Este script foi desenvolvido para análise de contigs em arquivos FASTA no contexto de bioinformática.

