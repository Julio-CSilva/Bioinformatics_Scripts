# Análise Estatística de Contigs

O script `analysis_contig.py` realiza a análise estatística de arquivos
`.fasta`/`.fa`, calculando, **para cada contig**, a composição de nucleotídeos:

- **%AT**: porcentagem de Adenina (A) e Timina (T).
- **%GC**: porcentagem de Guanina (G) e Citosina (C).
- **AT Skew**: viés entre Adenina e Timina — `(A − T) / (A + T)`.
- **GC Skew**: viés entre Guanina e Citosina — `(G − C) / (G + C)`.

Os resultados são gravados em um arquivo `.csv`.

## Requisitos

- Python 3
- [`python-dotenv`](https://pypi.org/project/python-dotenv/) — instale com
  `pip install -r ../requirements.txt`
- Um arquivo `.env` com as variáveis de ambiente descritas abaixo.

### Configuração (`.env`)

O script carrega as configurações de `../../samples/.env` (dois níveis acima do
script). Veja o modelo em [`.env.example`](../.env.example) na raiz do
repositório. Variáveis utilizadas:

| Variável                | Descrição                                                                 |
|-------------------------|---------------------------------------------------------------------------|
| `NOVOPLASTY_FASTA_PATH` | Diretório de entrada com os arquivos `.fa`/`.fasta`                        |
| `PATH_RESULTS`          | Diretório base de saída; o CSV é salvo em `Table/Novoplasty_analysis_contigs.csv` |

## Como Usar

O script não recebe argumentos de linha de comando; a configuração vem do `.env`.

```sh
python3 analysis_contig.py
```

## Estrutura do Arquivo de Saída

O CSV gerado tem as seguintes colunas:

| Coluna     | Descrição                                                  |
|------------|------------------------------------------------------------|
| `File`     | Nome do arquivo FASTA                                      |
| `Contigs`  | Nome da espécie, extraído do nome do arquivo (após o `_`)  |
| `Amount`   | Número de bases da contig                                  |
| `%AT`      | Porcentagem de A + T                                       |
| `AT Skew`  | Índice AT Skew                                             |
| `%GC`      | Porcentagem de G + C                                       |
| `GC Skew`  | Índice GC Skew                                             |

## Exemplo de Saída

```csv
File,Contigs,Amount,%AT,AT Skew,%GC,GC Skew
ERR123_EspecieAlpha.fa,EspecieAlpha,16542,55.60,0.10,44.40,-0.03
ERR456_EspecieBeta.fa,EspecieBeta,16780,53.20,0.08,46.80,-0.01
```

## Observações

- O arquivo de saída é sobrescrito a cada execução.
- A subpasta `Table/` precisa existir dentro de `PATH_RESULTS`.

## Autor

Julio-CSilva
