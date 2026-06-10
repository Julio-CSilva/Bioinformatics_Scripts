import os
from pathlib import Path
import argparse

def renomear_arquivos_assembly(diretorio_raiz):
    # Converte o caminho para um objeto Path
    base_path = Path(diretorio_raiz)
    
    if not base_path.is_dir():
        print(f"Erro: O diretório '{diretorio_raiz}' não foi encontrado.")
        return

    print(f"Iniciando processamento em: {base_path.absolute()}\n")

    # Percorre todas as pastas dentro do diretório raiz
    for pasta in base_path.iterdir():
        if pasta.is_dir():
            nome_da_pasta = pasta.name
            
            # Define os arquivos que queremos renomear
            alvos = {
                "assembly.fasta": f"{nome_da_pasta}.fa",
                "assembly.gfa": f"{nome_da_pasta}.gfa"
            }
            
            for nome_antigo, nome_novo in alvos.items():
                caminho_antigo = pasta / nome_antigo
                caminho_novo = pasta / nome_novo
                
                # Verifica se o arquivo original existe antes de renomear
                if caminho_antigo.exists():
                    try:
                        caminho_antigo.rename(caminho_novo)
                        print(f"[OK] {nome_antigo} -> {nome_novo}")
                    except Exception as e:
                        print(f"[ERRO] Falha ao renomear {caminho_antigo}: {e}")
                else:
                    print(f"[AVISO] Arquivo não encontrado em: {pasta.name}/{nome_antigo}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Renomeia os arquivos assembly.fasta e assembly.gfa para o nome da pasta.")
    parser.add_argument("-u", "--unicycler", required=True, help="Diretório das montagens do Unicycler")

    args = parser.parse_args()
    renomear_arquivos_assembly(args.unicycler)