# README - Processamento de Arquivos de Texto

Este projeto contém dois scripts, `split.py` e `merge.py`, que trabalham em conjunto para dividir e mesclar arquivos de texto que contém informações de Tandem Repeats, em diretórios organizados.

## 1. split.py - Divisão de Arquivos

### Funcionalidade
O script `split.py` espera receber um arquivo .txt com dados de Tandem, de uma unica espécie ou conjunto de espécies, separando os e gerando um arquivo para cada.

### Como Usar
1. Coloque os arquivos de texto na pasta definida em `files_tr`.
2. Execute o script `split.py` 

## 2. merge.py - Mesclagem de Arquivos

### Funcionalidade
O script `merge.py` mescla arquivos de texto organizados nos subdiretórios criados pelo `split.py`.

### Como Usar
1. Certifique-se de que os arquivos estejam organizados dentro da pasta `separeted`.
2. Execute o script `merge.py`.
3. Ele criará arquivos mesclados na pasta `merged/`, agrupando os conteúdos dos arquivos por diretório.

## Requisitos
- Python 3.x

## Observações
- Se um diretório tiver apenas um arquivo, ele será movido diretamente sem mesclagem.
- O nome dos arquivos gerados segue o nome do diretório onde estavam os arquivos originais.

Esses scripts são úteis para organizar grandes conjuntos de arquivos e processá-los de forma eficiente.
