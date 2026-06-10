# Bioinformatics Scripts

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20634469.svg)](https://doi.org/10.5281/zenodo.20634469)

Coleção de scripts utilitários para tarefas de bioinformática — manipulação de
arquivos FASTA, montagens de genomas mitocondriais, anotações `.bed`, BLAST
local e organização de arquivos. Cada pasta é uma ferramenta independente e
contém seu próprio `README.md` com instruções detalhadas.

## Ferramentas

| Ferramenta | Descrição |
|------------|-----------|
| 📂 [analysis_contigs](./analysis_contigs) | Calcula estatísticas de composição (%AT, %GC, AT/GC Skew) de cada contig em arquivos FASTA e exporta para CSV. |
| 📂 [count_bases](./count_bases) | Conta o total de bases de vários FASTA em paralelo, a partir de uma lista `SRA:ESPECIE`, gerando um relatório CSV. |
| 📂 [extrator_genes](./extrator_genes) | Extrai contigs/genes específicos (ou todos) de arquivos FASTA, salvando cada um em um arquivo separado. |
| 📂 [processing_fa](./processing_fa) | Mantém apenas a maior contig de cada FASTA e padroniza o cabeçalho com o nome do arquivo. |
| 📂 [comparisionFasta_with_blastLocal](./comparisionFasta_with_blastLocal) | Análises de similaridade com BLAST+ local: pares da mesma espécie e comparação entre montagens (NOVOPlasty × Unicycler). |
| 📂 [Unicycler_files_treatment](./Unicycler_files_treatment) | Renomeia as saídas do montador Unicycler (`assembly.fasta`/`.gfa`) para o nome da pasta de cada amostra. |
| 📂 [altername_mitos2_galaxy](./altername_mitos2_galaxy) | Renomeia arquivos de saída do Mitos2 Galaxy com base em um dicionário de identificadores. |
| 📂 [checker_BEDfile](./checker_BEDfile) | Valida arquivos `.bed` de genomas mitocondriais (38 anotações), ajusta o Dloop e move os completos para `verified/`. |
| 📂 [merged_and_split_tr](./merged_and_split_tr) | Divide e remonta arquivos de *Tandem Repeats* organizados por espécie. |
| 📂 [mv_file](./mv_file) | Organiza arquivos em pastas por grupos de espécies definidos em uma lista. |
| 📂 [variation_trna_files](./variation_trna_files) | Compara conjuntos de arquivos de tRNA entre amostras de uma mesma espécie e registra as variações. |

## Requisitos gerais

- **Python 3** (algumas ferramentas exigem **3.12+** — indicado no README de cada uma).
- **[python-dotenv](https://pypi.org/project/python-dotenv/)** — usado por `analysis_contigs` e `count_bases`. Instale com:

  ```sh
  pip install -r requirements.txt
  ```
- **BLAST+** (NCBI) instalado no sistema (`blastn`, `makeblastdb`) — necessário
  apenas para a ferramenta `comparisionFasta_with_blastLocal`.

A maioria dos scripts usa somente a biblioteca padrão do Python.

## Configuração (`.env`)

As ferramentas `analysis_contigs` e `count_bases` leem caminhos a partir de um
arquivo `.env`. Copie o modelo [`.env.example`](./.env.example) e preencha com
os caminhos da sua máquina. **Os scripts esperam o `.env` em `../../samples/.env`**
(dois níveis acima do script) — veja os detalhes no próprio `.env.example`. O
`.env` real nunca deve ser versionado.

## Dados de entrada

As pastas de dados (FASTA, FASTQ, `.bed`, saídas do Unicycler etc.) **não** são
versionadas — devem ser fornecidas localmente pelo usuário. Consulte o
[`.gitignore`](./.gitignore) para ver o que é ignorado.

## Licença

Distribuído sob a licença [MIT](./LICENSE).

## Contato

Dúvidas ou sugestões? Abra uma *issue* neste repositório.

---
Repositório em constante atualização à medida que novos scripts são adicionados.
