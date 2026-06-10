# Análise de Similaridade Local (BLAST)

Esta pasta contém dois scripts Python que utilizam o **BLAST+** (Basic Local
Alignment Search Tool) para medir a similaridade entre arquivos FASTA.

## Requisitos (para ambos os scripts)

- Python 3
- **BLAST+** instalado, com `blastn` e `makeblastdb` disponíveis no `PATH`
  (ex.: `sudo apt install ncbi-blast+` ou `conda install -c bioconda blast`).

---

## 1. `blastBetweenEspecies.py` — Comparação pareada dentro da mesma espécie

### Funcionalidade

Compara **todos os pares** de arquivos FASTA pertencentes à mesma espécie,
dentro de um único diretório. Para cada par:

1. Cria um banco de dados BLAST temporário em `.tmp/temp_blast_db` a partir de
   um dos arquivos (*Subject*).
2. Roda o `blastn` do outro arquivo (*Query*) contra esse banco.
3. Calcula a **identidade média** dos hits encontrados.
4. Remove os arquivos temporários do banco (`.nhr`, `.nin`, `.nsq`).

### Como Usar

Crie a pasta `.tmp/` (usada para os bancos temporários) e execute, passando dois
argumentos posicionais:

```sh
mkdir -p .tmp
python3 blastBetweenEspecies.py <arquivo_lista_especies.txt> <diretorio_fasta>
```

- `<arquivo_lista_especies.txt>`: uma espécie por linha (ver `sample_list.txt`).
- `<diretorio_fasta>`: diretório com os arquivos `*<especie>*.fasta`.

Espécies com menos de 2 arquivos são puladas.

### Saída

Imprime no console, para cada par comparado, os nomes dos arquivos e a
porcentagem de identidade média.

---

## 2. `blastBetweenSamples.py` — Comparação entre montagens (NOVOPlasty × Unicycler)

### Funcionalidade

Compara montagens correspondentes entre dois diretórios, pareando arquivos pelo
prefixo `<SRA>_<especie>`. O arquivo do NOVOPlasty é usado como **Query** e o do
Unicycler como **Subject**, executando `blastn` diretamente (opção `-subject`,
sem criar banco). Para cada par, registra o melhor hit.

### Como Usar

```sh
python3 blastBetweenSamples.py -n <dir_novoplasty> -u <dir_unicycler> [-o saida.csv]
```

| Argumento           | Obrigatório | Descrição                                              |
|---------------------|:-----------:|--------------------------------------------------------|
| `-n`, `--novoplasty`|     Sim     | Diretório das montagens do NOVOPlasty (Query)          |
| `-u`, `--unicycler` |     Sim     | Diretório das montagens do Unicycler (Subject)         |
| `-o`, `--output`    |     Não     | CSV de saída (padrão: `resultado_blast_montagens.csv`) |

### Saída

CSV com uma linha por par comparado e as colunas:

| Coluna     | Descrição                                          |
|------------|----------------------------------------------------|
| `sra`      | Identificador SRA                                  |
| `specie`   | Nome da espécie                                    |
| `len_novo` | Comprimento total da sequência (NOVOPlasty)        |
| `len_uni`  | Comprimento total da sequência (Unicycler)         |
| `pident`   | Identidade percentual do melhor hit                |
| `qcovs`    | Cobertura da query (%)                             |
| `evalue`   | E-value do melhor hit                              |

## Observações

- O arquivo `sample_list.txt` é um exemplo de lista de espécies.
- As pastas de dados (`fasta_files/`, `.tmp/`) não são versionadas.
- Os scripts usam f-strings com aspas aninhadas, exigindo **Python 3.12+**.

## Autor

Julio-CSilva
