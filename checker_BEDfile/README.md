# Verificação e Modificação de Arquivos .BED

O script `verify_bed_files.py` verifica arquivos `.bed`, ajusta Dloop e verifica Genes, TRNA e RRNA. `.bed` que estiverem completos são movidos para um diretório verificado.

## Como Funciona

1. **Lê e modifica os arquivos `.bed`**:
   - Substitui a primeira coluna pelo nome do arquivo.
   - Garante que o gene `Dloop` tenha a orientação `+`.

2. **Verifica se o arquivo contém todos os genes esperados** e possui **38 linhas(13 Genes, 22 Trna, 2 Rrna e Dloop)**.

3. **Move os arquivos validados** para a pasta `verified/`.

## Requisitos

- Python instalado
- Diretório `beds/` contendo os arquivos `.bed` a serem verificados

## Como Usar

1. **Defina os diretórios e execute o script**:
   ```sh
   python3 verify_bed.py
   ```

2. **Saída esperada**:
   - O script exibirá mensagens indicando genes ausentes ou splitados.
   - Arquivos completos serão movidos para `verified/`.

## Exemplo de Uso

### Arquivos `.bed` antes:
```
sample1.bed
sample2.bed
```

### Após a execução:
```
verified/
  ├── sample1.bed
  ├── sample2.bed
```

### Mensagens exibidas:
```
Arquivo: sample1.bed - Genes ausentes: trnP(tgg)
Arquivo: sample2.bed - Genes splitados: nad4
```

## Cuidados

- Caso um gene esteja ausente, o arquivo não será movido para `verified/`.
- Se o gene `Dloop` estiver faltando, será adicionado automaticamente(Padrão: 18892).
- Genes splitados (ex.: `gene_0`) serão reconhecidos.

## Autor
Este script foi criado para facilitar a curadoria e validação de arquivos `.bed` em bioinformática.

