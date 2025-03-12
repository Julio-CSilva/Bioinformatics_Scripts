import os
import re

dir_path = "Arquivos" # Defina os caminhos da pasta e do arquivo de lista
arquivo_lista = "dictionary.txt" # Arquivo com o mapeamento de identificadores para novos nomes no formato chave: valor

# Verificar se a pasta existe
if not os.path.exists(dir_path):
    print(f"Erro: Pasta '{dir_path}' não encontrada.")
    exit()

# 1. Ler a lista.txt e criar um dicionário {identificador: novo_nome}
mapeamento_nomes = {}
try:
    with open(arquivo_lista, "r", encoding="utf-8") as lista:
        for linha in lista:
            partes = linha.strip().split(": ")
            if len(partes) == 2:
                identificador, novo_nome = partes
                novo_nome_sem_extensao = os.path.splitext(novo_nome)[0]  # Remove a extensão se houver
                mapeamento_nomes[identificador] = novo_nome_sem_extensao
except FileNotFoundError:
    print(f"Erro: Arquivo '{arquivo_lista}' não encontrado.")
    exit()

# 2. Percorrer os arquivos na pasta e renomear com base no número identificado
for filename in os.listdir(dir_path):
    match = re.search(r'_(\d+)_', filename)  # Captura o número no padrão _NUMERO_
    if match:
        identificador = match.group(1)

        if identificador in mapeamento_nomes:
            caminho_antigo = os.path.join(dir_path, filename)
            extensao = os.path.splitext(filename)[1]  # Mantém a extensão original
            nome_novo = os.path.join(dir_path, f"{mapeamento_nomes[identificador]}{extensao}")

            # Verificar se o nome novo já existe para evitar sobrescrita acidental
            if os.path.exists(nome_novo):
                print(f"Aviso: Arquivo '{nome_novo}' já existe. Pulando renomeação.")
                continue

            # Renomear o arquivo
            try:
                os.rename(caminho_antigo, nome_novo)
                print(f"Renomeado: {filename} -> {mapeamento_nomes[identificador]}{extensao}")
            except Exception as e:
                print(f"Erro ao renomear '{filename}': {e}")

print("Renomeação concluída!")
