# Renomeação de Arquivos Resultados do Mitos2 Galaxy

O script `rename_files.py` renomeia arquivos de saída do Mitos2 Galaxy em um diretório com base em um mapeamento definido em um arquivo de dicionário (`dicionario.txt`).

## Como Funciona

1. **Lê um arquivo de mapeamento** (`dicionario.txt`), onde cada linha contém um identificador e um novo nome no formato:
   ```
   123: Nome_x
   456: Nome_y
   ```

2. **Percorre os arquivos do diretório** e identifica aqueles que contêm um número no formato `_NUMERO_` dentro do nome do arquivo.

3. **Renomeia os arquivos** de acordo com o dicionário, mantendo a extensão original.

## Requisitos

- Python instalado
- Um diretório contendo os arquivos a serem renomeados
- Um arquivo `dicionario.txt` com o mapeamento de nomes

## Como Usar

1. **Defina o diretório dos arquivos a serem renomeados**:
   ```python
   dir_path = "Arquivos"
   ```

2. **Defina o nome do arquivo de dicionário**:
   ```python
   arquivo_lista = "dicionario.txt"
   ```

3. **Execute o script**:
   ```sh
   python3 rename_files.py
   ```

## Exemplo de Uso

### Arquivos na pasta `Arquivos/` antes da execução:
```
exemplo_123_.txt
dados_456_.csv
```

### `dicionario.txt`:
```
123: RelatorioFinal
456: AnaliseDados
```

### Após a execução do script:
```
RelatorioFinal.txt
AnaliseDados.csv
```

## Cuidados

- O script evita sobrescrever arquivos já existentes.
- Caso um identificador não esteja no `dicionario.txt`, o arquivo original não será renomeado.

## Autor
Este script foi desenvolvido para facilitar a organização e renomeação automática de arquivos em bioinformática ou outras aplicações.

