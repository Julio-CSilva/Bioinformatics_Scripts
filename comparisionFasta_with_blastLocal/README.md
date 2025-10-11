### Análise de Similaridade Local (BLAST)

Esta pasta contém dois scripts Python que utilizam ferramentas BLAST+ (Basic Local Alignment Search Tool) para realizar análises de similaridade em arquivos FASTA.

## 1. Comparação Pareada entre Membros da Mesma Espécie (`blastBetweenEspecies.py`)

### Funcionalidade
O script compara todos os pares de arquivos FASTA que pertencem à mesma espécie (identificada em um arquivo de lista de entrada) dentro de um diretório. Ele segue as seguintes etapas:
1. Encontra arquivos FASTA para cada espécie listada.
2. Para cada par, cria um banco de dados BLAST temporário (`.tmp/temp_blast_db`) com o arquivo *Subject*.
3. Roda o `blastn` e calcula a porcentagem de identidade média dos melhores *hits* entre os pares.
4. Limpa os arquivos temporários do banco de dados.

### Requisitos

- Python instalado
- BLAST+ instalado (para `makeblastdb` e `blastn`)
- Um arquivo de lista com os nomes das espécies.
- Um diretório contendo os arquivos FASTA das espécies.

### Como Usar

1. **Defina os argumentos de entrada**:
   - O caminho para o arquivo com a lista de espécies (ex: `list_species.txt`).
   - O caminho para o diretório contendo os arquivos FASTA (ex: `dir_fastas`).

2. **Execute o script**:
   ```sh
   python3 blastBetweenEspecies.py <arquivo_lista_especies.txt> <diretorio_fasta>
    ````

### Saída Esperada

O script imprime no console o status da comparação de cada par, incluindo o nome dos arquivos e a porcentagem de identidade.

## 2\. Comparação de Arquivos em Diretórios Distintos (`blastBetweenSamples.py`)

### Funcionalidade

O script compara arquivos FASTA que possuem o mesmo nome, mas estão localizados em dois diretórios distintos. Ele trata o primeiro diretório (`dir1`) como **Query** e o segundo (`dir2`) como **Subject**, utilizando o `blastn` via biblioteca Biopython para reportar o nível de similaridade.

### Requisitos

  - Python instalado
  - BLAST+ instalado
  - Biblioteca **Biopython** (que contém `Bio.SeqIO` e `Bio.Blast`)
  - Dois diretórios com arquivos FASTA correspondentes por nome.

### Como Usar

1.  **Defina os argumentos de entrada**:

      - O caminho para o diretório da Query (`dir1`).
      - O caminho para o diretório do Subject (`dir2`).

2.  **Execute o script**:

    ```sh
    python3 blastBetweenSamples.py <diretorio_query> <diretorio_subject>
    ```

### Saída Esperada

O script imprime no console os resultados detalhados da comparação BLAST para cada par de arquivos encontrados, incluindo:

  - Status da comparação (ex: "Match BLAST" ou "sem alinhamento BLAST")
  - Porcentagem de Similaridade (Identidade)
  - Cobertura da Query
  - E-value