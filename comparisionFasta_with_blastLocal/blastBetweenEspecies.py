import os
import sys
import subprocess
from itertools import combinations
import glob

def encontrar_arquivos_fasta(diretorio_fasta, nome_especie):
    """Encontra todos os arquivos .fasta para uma determinada espécie em um diretório."""
    # Usamos glob para encontrar arquivos que contenham o nome da espécie
    # Isso torna o script flexível para nomes como SRA_NOMEESPECIE.fasta ou SRA_NOMEESPECIE_1.fasta
    padrao_busca = os.path.join(diretorio_fasta, f"*{nome_especie}*.fasta")
    arquivos_encontrados = glob.glob(padrao_busca)
    return arquivos_encontrados

def executar_blast_pareado(arquivo_query, arquivo_db):
    """
    Executa o BLASTN entre dois arquivos.
    1. Cria um banco de dados temporário com o arquivo_db.
    2. Roda o blastn com o arquivo_query contra o banco de dados.
    3. Extrai a identidade média dos melhores hits.
    4. Limpa os arquivos de banco de dados temporários.
    """
    db_name = ".tmp/temp_blast_db"
    
    # 1. Criar o banco de dados BLAST a partir de um dos arquivos
    comando_makedb = [
        "makeblastdb",
        "-in", arquivo_db,
        "-dbtype", "nucl",
        "-out", db_name
    ]
    
    # 2. Executar o BLASTN
    # Usamos o formato de saída 6 (tabular) e pedimos apenas o percentual de identidade (pident)
    comando_blastn = [
        "blastn",
        "-query", arquivo_query,
        "-db", db_name,
        "-outfmt", "6 pident"
    ]

    identidade_media = 0.0

    try:
        # Roda o makeblastdb
        subprocess.run(comando_makedb, check=True, capture_output=True, text=True)
        
        # Roda o blastn
        resultado = subprocess.run(comando_blastn, check=True, capture_output=True, text=True)
        
        # 3. Processar o resultado
        linhas = resultado.stdout.strip().split('\n')
        if linhas and linhas[0]: # Verifica se houve algum hit
            soma_identidades = sum(float(linha.strip()) for linha in linhas)
            identidade_media = soma_identidades / len(linhas)
        else:
            identidade_media = 0.0 # Nenhum hit encontrado

    except subprocess.CalledProcessError as e:
        print(f"  [ERRO] Ocorreu um erro ao executar o BLAST:")
        print(f"  Comando: {' '.join(e.cmd)}")
        print(f"  Stderr: {e.stderr}")
        return None
    except Exception as e:
        print(f"  [ERRO] Um erro inesperado ocorreu: {e}")
        return None
    finally:
        # 4. Limpar arquivos de banco de dados temporários
        extensoes_db = ['.nhr', '.nin', '.nsq']
        for ext in extensoes_db:
            if os.path.exists(db_name + ext):
                os.remove(db_name + ext)

    return identidade_media

def main():
    if len(sys.argv) != 3:
        print("Uso: python analise_blast_local.py <arquivo_lista_especies.txt> <diretorio_fasta>")
        sys.exit(1)

    arquivo_especies = sys.argv[1]
    diretorio_fasta = sys.argv[2]

    if not os.path.isfile(arquivo_especies):
        print(f"Erro: O arquivo de espécies '{arquivo_especies}' não foi encontrado.")
        sys.exit(1)
    
    if not os.path.isdir(diretorio_fasta):
        print(f"Erro: O diretório de fastas '{diretorio_fasta}' não foi encontrado.")
        sys.exit(1)

    print("--- Iniciando Análise de BLAST Local dos membros da mesma espécie ---")

    with open(arquivo_especies, 'r') as f:
        especies = [linha.strip() for linha in f if linha.strip()]

    for especie in especies:
        print(f"\n[PROCESSANDO ESPÉCIE]: {especie}")
        
        arquivos_fasta = encontrar_arquivos_fasta(diretorio_fasta, especie)
        
        if len(arquivos_fasta) < 2:
            print(f"  -> Encontrado apenas {len(arquivos_fasta)} arquivo(s). Pulando para a próxima espécie.")
            continue
        
        print(f"  -> Encontrados {len(arquivos_fasta)} arquivos. Realizando comparações pareadas...")
        
        # Gera todas as combinações únicas de 2 arquivos
        pares_para_comparar = list(combinations(arquivos_fasta, 2))
        
        for par in pares_para_comparar:
            arquivo1, arquivo2 = par
            nome_arq1 = os.path.basename(arquivo1)
            nome_arq2 = os.path.basename(arquivo2)
            
            print(f"  - Comparando: '{nome_arq1}' vs '{nome_arq2}'")
            
            identidade = executar_blast_pareado(arquivo1, arquivo2)

            if identidade is not None:
                print(f"    -> Identidade: {identidade:.2f}%")
            else:
                print("    -> Falha na comparação.")

    print("\n--- Análise Concluída ---")

if __name__ == "__main__":
    main()