# Renomeação de Arquivos Resultados do Mitos2 Galaxy

O script `rename_files.py` renomeia arquivos de saída do Mitos2 Galaxy em um diretório com base em um mapeamento definido em um arquivo de dicionário (`dictionary.txt`).

## Como Funciona

1. **Lê um arquivo de mapeamento** (`dictionary.txt`), onde cada linha contém um identificador e um novo nome no formato:
   ```
   123: Nome_x
   456: Nome_y
   ```

2. **Percorre os arquivos do diretório** e identifica aqueles que contêm um número no formato `_NUMERO_` dentro do nome do arquivo.

3. **Renomeia os arquivos** de acordo com o dicionário, mantendo a extensão original.

## Requisitos

- Python 3 (utiliza apenas a biblioteca padrão: `os`, `re`)
- Um diretório contendo os arquivos a serem renomeados
- Um arquivo `dictionary.txt` com o mapeamento de nomes

> Por padrão o script procura os arquivos na pasta `Arquivos/` e o dicionário em
> `dictionary.txt`. Ajuste as variáveis `dir_path` e `arquivo_lista` no início do
> script conforme a sua estrutura.

## Como Usar

1. **Defina o diretório dos arquivos a serem renomeados**:
   ```python
   dir_path = "Arquivos"
   ```

2. **Defina o nome do arquivo de dicionário**:
   ```python
   arquivo_lista = "dictionary.txt"
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

### `dictionary.txt`:
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
- Caso um identificador não esteja no `dictionary.txt`, o arquivo original não será renomeado.

## Autor

Julio-CSilva

