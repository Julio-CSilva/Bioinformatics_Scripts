# Análise de Variação de Arquivos tRNA

Este script Python analisa e compara arquivos em diretórios organizados por espécies para identificar variações nos arquivos entre diferentes membros de uma mesma espécie.

## Estrutura do Diretório de Entrada
O diretório esperado para a análise deve estar organizado com subpastas nomeadas de acordo com o seguinte padrão:

```
variation_trna_files/
    trna_files/
        Codigo1 - EspecieA/ or Codigo1_EspecieA/
        Codigo2 - EspecieB/ or Codigo2_EspecieB/
        Codigo3 - EspecieC/ or Codigo3_EspecieC/
        ...
```
Cada pasta deve conter arquivos correspondentes aos Trna daquela espécie.

## Como Funciona
O script executa as seguintes etapas:

1. **Agrupamento por Espécie:**
   - As subpastas são lidas e agrupadas com base no nome da espécie.
   - O agrupamento é feito considerando o segundo elemento do nome da pasta (após um " - " ou "_").

2. **Comparar arquivos entre grupos da mesma espécie:**
   - Para cada espécie, compara os arquivos entre todas as suas subpastas.
   - Identifica diferenças entre os arquivos presentes em diferentes subpastas da mesma espécie.
   - Registra as variações em `variation_trna_files/result_variation.txt`.

## Execução

Certifique-se de que o Python está instalado e execute o script com:

```bash
python3 main.py
```

## Dependências
- Nenhuma biblioteca externa é necessária. Apenas as bibliotecas padrões do Python são utilizadas:
  - `os`
  - `collections.defaultdict`
  - `pathlib.Path`

## Saída

O script gerará um arquivo `variation_trna_files/result_variation.txt` contendo linhas no formato:

```
[Codigo1 - EspecieA] x [Codigo2 - EspecieA]	{'arquivo_diferente1.txt', 'arquivo_diferente2.txt'}
```

Isso indica que os arquivos listados estão presentes em uma subpasta, mas não na outra.

---

Este script é útil para análise de variações em arquivos entre grupos de uma mesma espécie em um conjunto de dados de tRNA.

