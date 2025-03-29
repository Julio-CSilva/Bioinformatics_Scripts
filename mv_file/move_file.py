import os
import shutil
from pathlib import Path


dir_origem = "mv_file/files" # Diretório dos arquivos
list_species = "mv_file/sort.txt" # Lista de nomes

def criar_pastas_e_mover_arquivos(diretorio_origem, list_species):
    # Ler o arquivo lista.txt e processar as espécies
    grupos = []
    grupo_atual = []

    with open(list_species, 'r') as file:
        for linha in file:
            linha = linha.strip()
            if linha == "----":
                if grupo_atual:
                    grupos.append(grupo_atual)
                    grupo_atual = []
            else:
                grupo_atual.append(linha)
        if grupo_atual:
            grupos.append(grupo_atual)  # Adicionar o último grupo

    # Agora criar as pastas e mover os arquivos
    for i, grupo in enumerate(grupos):
        nome_pasta = f'results/div_{i+1}'  # Nome da pasta do grupo (pode ser modificado conforme necessário)
        caminho_pasta = os.path.join("mv_file/", nome_pasta)
        os.makedirs(caminho_pasta, exist_ok=True)  # Cria a pasta se não existir

        for especie in grupo:
            # Substituir espaços por underscores na espécie para comparar com o nome do arquivo
            especie_arquivo = especie.replace(" ", "_").lower()

            for arquivo in os.listdir(diretorio_origem):
                if especie_arquivo in arquivo.lower():  # Verifica se o nome da espécie está no nome do arquivo
                    arquivo_origem = os.path.join(diretorio_origem, arquivo)
                    arquivo_destino = os.path.join(caminho_pasta, arquivo)
                    shutil.move(arquivo_origem, arquivo_destino)  # Move o arquivo

dir_origem = Path(dir_origem).absolute()
list_species = Path(list_species).absolute()
# Chama a função para mover os arquivos
criar_pastas_e_mover_arquivos(dir_origem, list_species)
