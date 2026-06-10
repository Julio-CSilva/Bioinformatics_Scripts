import os
import csv
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed
from typing import List, Dict
from dotenv import load_dotenv

# Carregamento do .env
env_path = os.path.join(os.path.dirname(__file__), '..', '..', 'samples', '.env')
load_dotenv(dotenv_path=env_path)

SRA_SPECIES_FILE = os.getenv("dict_SRA-Species_orderby_nameSpecies_az")
PATH_RESULTS = os.getenv("PATH_RESULTS")
UNICYCLER_FASTA_PATH = os.getenv("UNICYCLER_FASTA_PATH")

def contar_bases_fasta(caminho_arquivo: Path) -> int:
    """Conta o número total de bases (nucleotídeos) em um arquivo FASTA de forma eficiente."""
    total_bases = 0
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            for linha in f:
                if not linha.startswith('>'):
                    total_bases += len(linha.strip())
        return total_bases
    except FileNotFoundError:
        return -1

def processar_item(item: str, diretorio_fasta: Path) -> Dict[str, any]:
    """Processa um único item da lista no formato 'SRA:ESPECIE'."""
    try:
        sra, especie = item.split(':', 1)
        sra = sra.strip()
        especie = especie.strip()
    except ValueError:
        return {"item": item, "sra": None, "especie": None, "bases": -1, "status": "Formato inválido"}

    nome_arquivo = f"{sra}_{especie}.fa"
    
    # REVISÃO: Usando o objeto Path para unir o diretório e o nome do arquivo com segurança
    arquivo_fasta = diretorio_fasta / nome_arquivo
    
    bases = contar_bases_fasta(arquivo_fasta)
    
    if bases == -1:
        status = "Arquivo não encontrado"
    else:
        status = "Sucesso"
        
    return {
        "item": item,
        "sra": sra,
        "especie": especie,
        "bases": bases,
        "status": status
    }

def analisar_arquivos_fasta(lista_entradas: List[str], caminho_pasta: str, arquivo_saida: Path):
    diretorio_fasta = Path(caminho_pasta)
    resultados = []

    cores_disponiveis = os.cpu_count() or 1
    print(f"Iniciando a leitura utilizando até {cores_disponiveis} núcleos...")

    with ProcessPoolExecutor(max_workers=cores_disponiveis) as executor:
        futuros = [executor.submit(processar_item, item, diretorio_fasta) for item in lista_entradas]
        
        for futuro in as_completed(futuros):
            resultados.append(futuro.result())

    # REVISÃO: Garante que a pasta de destino do CSV (ex: /Table/) exista antes de salvar
    arquivo_saida.parent.mkdir(parents=True, exist_ok=True)

    try:
        with open(arquivo_saida, mode='w', newline='', encoding='utf-8') as f_csv:
            escritor = csv.writer(f_csv, delimiter=',')
            escritor.writerow(['SRA', 'Especie', 'Total_Bases', 'Status'])
            
            for res in resultados:
                sra_nome = res.get('sra', 'N/A')
                especie_nome = res.get('especie', 'N/A')
                total_bases = res['bases'] if res['status'] == "Sucesso" else ''
                status_arquivo = res['status']
                
                escritor.writerow([sra_nome, especie_nome, total_bases, status_arquivo])

        print(f"\nProcessamento concluído. Resultados salvos em: {arquivo_saida}")
        
    except Exception as e:
        print(f"\nErro ao tentar salvar o arquivo CSV: {e}")

if __name__ == "__main__":
    # Validação de segurança para garantir que o .env carregou corretamente
    if not all([SRA_SPECIES_FILE, PATH_RESULTS, UNICYCLER_FASTA_PATH]):
        print("Erro: Variáveis do .env ausentes. Verifique o caminho e o conteúdo do .env.")
        exit(1)

    # REVISÃO: Lê o arquivo .txt e transforma as linhas numa lista do Python
    lista_de_especies = []
    try:
        with open(SRA_SPECIES_FILE, 'r', encoding='utf-8') as f:
            lista_de_especies = [linha.strip() for linha in f if linha.strip()]
    except FileNotFoundError:
        print(f"Erro: Arquivo de lista não encontrado em {SRA_SPECIES_FILE}")
        exit(1)

    # REVISÃO: Montagem do caminho de saída usando Path
    caminho_saida_csv = Path(PATH_RESULTS) / "Table" / "resultados_contagem_bases_UNICYCLER.csv"

    analisar_arquivos_fasta(lista_de_especies, UNICYCLER_FASTA_PATH, caminho_saida_csv)