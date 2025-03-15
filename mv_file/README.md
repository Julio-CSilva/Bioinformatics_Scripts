# Organização de Arquivos por Lista

Este script automatiza a organização de arquivos em diretórios específicos com base em uma lista. Ele lê uma lista estruturada e move os arquivos correspondentes para suas respectivas pastas.

## 📌 Funcionalidade
O script **move_file.py** lê um arquivo de texto contendo nomes agrupados e separados por **----** e move os arquivos correspondentes para pastas específicas dentro do diretório de origem.

## 📂 Estrutura do Projeto

```
📁 files
 ├── 📄 sort.txt    # Lista de espécies e divisores "----"
 ├── 📄 arquivo1.txt
 ├── 📄 arquivo2.txt
 ├── ...
 ├── 📁 files

```

## 🚀 Como Usar

### 1️⃣ Preparação dos Arquivos
- O **diretório de origem** deve conter os arquivos a serem organizados.
- O **arquivo `sort.txt`** deve conter os nomes, separados por `----` para indicar grupos. Exemplo:
  ```
  Especie A
  Especie B
  ----
  Especie C
  Especie D
  ```

### 2️⃣ Executando o Script
1. Certifique-se de que o script e os arquivos estão no mesmo diretório.
2. Edite as variáveis no início do script se necessário:
   ```python
   diretorio_origem = "files"  # Diretório dos arquivos
   lista_espécies = "sort.txt"  # Arquivo com a lista de espécies
   ```
3. Execute o script:
   ```sh
   python3 move_file.py
   ```

### 3️⃣ Resultado
- Os arquivos serão movidos para **pastas nomeadas como `div_X`** dentro de `results/`, conforme os grupos definidos no `sort.txt`.
- Se um arquivo corresponder a um nome de espécie, será movido para a pasta correta.

## 🛠 Requisitos
- Python 3.x
- Biblioteca `shutil` (padrão no Python)

## 📌 Observações
- Certifique-se de que os nomes no `sort.txt` correspondam corretamente aos nomes dos arquivos (ignora maiúsculas e substitui espaços por `_`).
- Arquivos não correspondentes permanecerão no diretório original.
