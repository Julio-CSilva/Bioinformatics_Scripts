# Unicycler Files Treatment

Script para padronizar os nomes dos arquivos de saída do montador de genomas
**Unicycler**. O Unicycler gera, em cada pasta de amostra, arquivos com nomes
genéricos (`assembly.fasta` e `assembly.gfa`). Este script renomeia esses
arquivos para o nome da pasta que os contém, facilitando a organização e a
identificação das montagens.

## Como Funciona

1. Recebe o caminho de um diretório raiz contendo várias subpastas de montagens.
2. Para **cada subpasta**, procura os arquivos:
   - `assembly.fasta` → renomeado para `<nome_da_pasta>.fa`
   - `assembly.gfa`   → renomeado para `<nome_da_pasta>.gfa`
3. Exibe o status de cada operação: `[OK]`, `[AVISO]` (arquivo não encontrado)
   ou `[ERRO]` (falha ao renomear).

## Requisitos

- Python 3 (utiliza apenas a biblioteca padrão: `os`, `pathlib`, `argparse`)

## Como Usar

```sh
python3 main.py -u <diretorio_das_montagens>
```

Argumentos:

| Argumento          | Obrigatório | Descrição                                     |
|--------------------|:-----------:|-----------------------------------------------|
| `-u`, `--unicycler`|     Sim     | Diretório que contém as subpastas de montagem |

## Exemplo

Estrutura **antes** da execução:

```
Unicycler/
├── ERR10768188_Heros_notatus/
│   ├── assembly.fasta
│   └── assembly.gfa
└── ERR10768189_Acarichthys_heckelii/
    ├── assembly.fasta
    └── assembly.gfa
```

Comando:

```sh
python3 main.py -u Unicycler
```

Estrutura **depois** da execução:

```
Unicycler/
├── ERR10768188_Heros_notatus/
│   ├── ERR10768188_Heros_notatus.fa
│   └── ERR10768188_Heros_notatus.gfa
└── ERR10768189_Acarichthys_heckelii/
    ├── ERR10768189_Acarichthys_heckelii.fa
    └── ERR10768189_Acarichthys_heckelii.gfa
```

## Observações

- A renomeação é **in-place** (substitui o nome do arquivo original).
- Apenas o primeiro nível de subpastas é percorrido.
- Os dados de montagem em si (FASTA/GFA e logs do Unicycler) **não** são
  versionados neste repositório — eles devem ser fornecidos localmente pelo
  usuário.

## Autor

Julio-CSilva
