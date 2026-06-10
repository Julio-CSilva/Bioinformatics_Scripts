# Count Bases

Script para contar o número total de bases (nucleotídeos) em arquivos FASTA.
A leitura é feita em **paralelo** (usando todos os núcleos disponíveis da CPU),
o que torna o processamento de muitos arquivos bastante rápido. O resultado é
salvo em um arquivo CSV.

## Como Funciona

1. Lê um arquivo de lista (texto) em que cada linha está no formato `SRA:ESPECIE`.
2. Para cada item, monta o nome de arquivo esperado `<SRA>_<ESPECIE>.fa` e o
   procura no diretório de FASTA configurado.
3. Conta todas as bases (todas as linhas que **não** começam com `>`).
4. Usa um `ProcessPoolExecutor` para processar os itens em paralelo.
5. Grava um CSV com uma linha por item, indicando o total de bases e o status.

## Requisitos

- Python 3
- [`python-dotenv`](https://pypi.org/project/python-dotenv/) — instale com
  `pip install -r ../requirements.txt`
- Um arquivo `.env` com as variáveis de ambiente descritas abaixo.

### Configuração (`.env`)

O script carrega as configurações de `../../samples/.env` (dois níveis acima do
script). Veja o modelo em [`.env.example`](../.env.example) na raiz do
repositório. Variáveis utilizadas:

| Variável                                   | Descrição                                                   |
|--------------------------------------------|-------------------------------------------------------------|
| `dict_SRA-Species_orderby_nameSpecies_az`  | Caminho do `.txt` com a lista `SRA:ESPECIE`                 |
| `UNICYCLER_FASTA_PATH`                      | Diretório onde estão os arquivos `<SRA>_<ESPECIE>.fa`       |
| `PATH_RESULTS`                             | Diretório base de saída (o CSV vai para a subpasta `Table/`)|

## Como Usar

O script não recebe argumentos de linha de comando; toda a configuração vem do
`.env`.

```sh
python3 main.py
```

### Formato do arquivo de lista (`SRA:ESPECIE`)

```
ERR10768188:Heros_notatus
ERR10768189:Acarichthys_heckelii
```

## Saída

CSV gravado em `<PATH_RESULTS>/Table/resultados_contagem_bases_UNICYCLER.csv`,
com as colunas:

| Coluna       | Descrição                                                    |
|--------------|--------------------------------------------------------------|
| `SRA`        | Identificador SRA                                            |
| `Especie`    | Nome da espécie                                              |
| `Total_Bases`| Número total de bases (vazio quando o status não é "Sucesso")|
| `Status`     | `Sucesso`, `Arquivo não encontrado` ou `Formato inválido`    |

Exemplo:

```csv
SRA,Especie,Total_Bases,Status
ERR10768188,Heros_notatus,16542,Sucesso
ERR10768189,Acarichthys_heckelii,,Arquivo não encontrado
```

## Observações

- Se alguma variável do `.env` estiver ausente, o script encerra com uma
  mensagem de erro.
- A pasta de saída (`Table/`) é criada automaticamente caso não exista.
- Os arquivos FASTA de entrada **não** são versionados neste repositório.

## Autor

Julio-CSilva
