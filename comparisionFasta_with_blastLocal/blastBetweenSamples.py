#!/usr/bin/env python3
import os
import csv
import re
import subprocess
import argparse

def calcular_comprimento_fasta(caminho_arquivo):
    """Calcula o comprimento total das sequências dentro de um arquivo FASTA."""
    total_len = 0
    try:
        with open(caminho_arquivo, 'r') as f:
            for line in f:
                if not line.startswith('>'):
                    total_len += len(line.strip())
    except Exception as e:
        print(f"Erro ao ler {caminho_arquivo}: {e}")
    return total_len

def extrair_sra_e_especie(nome_arquivo):
    """Extrai o SRA e o nome da espécie a partir do nome do arquivo (SRA_nome_da_especie.fasta)."""
    # Remove a extensão
    nome_base = os.path.splitext(nome_arquivo)[0]
    if nome_base.endswith('.fa'): # Trata caso splitext não tire tudo se houver pontos duplos
        nome_base = nome_base[:-3]
        
    # Separa pelo primeiro underline para isolar o SRA
    partes = nome_base.split('_', 1)
    if len(partes) == 2:
        return partes[0], partes[1]
    return None, None

def encontrar_arquivo_correspondente(diretorio, sra, especie):
    """Procura um arquivo no diretório que comece com SRA_especie e tenha extensão fa ou fasta."""
    prefixo = f"{sra}_{especie}"
    for arquivo in os.listdir(diretorio):
        if arquivo.startswith(prefixo):
            if arquivo.endswith(('.fa', '.fasta')):
                return os.path.join(diretorio, arquivo)
    return None

def executar_blastn(query_path, subject_path):
    """Executa o blastn local entre dois arquivos utilizando a opção -subject."""
    # Formato 6 customizado: pident (identidade), evalue, qcovs (cobertura da query), length (tamanho do alinhamento)
    comando = [
        "blastn",
        "-query", query_path,
        "-subject", subject_path,
        "-outfmt", "6 pident evalue qcovs length"
    ]
    
    try:
        resultado = subprocess.run(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        print(resultado)
        linhas = resultado.stdout.strip().split('\n')
        
        if linhas and linhas[0]:
            # Pega o melhor hit (primeira linha)
            valores = linhas[0].split('\t')
            return {
                "pident": valores[0],
                "evalue": valores[1],
                "qcovs": valores[2],
                "length": valores[3]
            }
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o BLAST entre {query_path} e {subject_path}: {e.stderr}")
    except Exception as e:
        print(f"Erro inesperado no BLAST: {e}")
        
    return {"pident": "N/A", "evalue": "N/A", "qcovs": "N/A", "length": "N/A"}

def main():
    parser = argparse.ArgumentParser(description="Compara montagens do NOVOPlasty e Unicycler via BLASTn.")
    parser.add_argument("-n", "--novoplasty", required=True, help="Diretório das montagens do NOVOPlasty")
    parser.add_argument("-u", "--unicycler", required=True, help="Diretório das montagens do Unicycler")
    parser.add_argument("-o", "--output", default="resultado_blast_montagens.csv", help="Nome do arquivo CSV de saída")
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.novoplasty) or not os.path.isdir(args.unicycler):
        print("Erro: Certifique-se de que ambos os caminhos fornecidos são diretórios válidos.")
        return

    dados_finais = []
    arquivos_novoplasty = [f for f in os.listdir(args.novoplasty) if f.endswith(('.fa', '.fasta'))]
    
    print(f"Encontrados {len(arquivos_novoplasty)} arquivos FASTA no diretório NOVOPlasty.")
    print("Iniciando as comparações...")

    for arq_novo in arquivos_novoplasty:
        sra, especie = extrair_sra_e_especie(arq_novo)
        if not sra or not especie:
            print(f"Aviso: Não foi possível extrair SRA/Espécie do arquivo {arq_novo}. Pulando...")
            continue
            
        caminho_novo = os.path.join(args.novoplasty, arq_novo)
        caminho_uni = encontrar_arquivo_correspondente(args.unicycler, sra, especie)
        
        if not caminho_uni:
            print(f"Aviso: Correspondente para {sra}_{especie} não foi encontrado no diretório Unicycler. Pulando...")
            continue
            
        # Calcula comprimentos das sequências
        len_novo = calcular_comprimento_fasta(caminho_novo)
        len_uni = calcular_comprimento_fasta(caminho_uni)
        
        # Executa BLAST
        print(f"Rodando BLASTn para: {sra} - {especie}...")
        blast_res = executar_blastn(query_path=caminho_novo, subject_path=caminho_uni)
        
        # Cobertura calculada (Alinhamento / Tamanho Query) como alternativa/complemento
        # Se qcovs já faz isso, podemos usar o valor do qcovs diretamente para a coluna 'cobertura'
        cobertura = blast_res["qcovs"]
        
        dados_finais.append({
            "sra": sra,
            "specie": especie,
            "len_novo": len_novo,
            "len_uni": len_uni,
            "pident": f"{float(blast_res["pident"]):.1f}%",
            "qcovs": blast_res["qcovs"] + "%",
            "evalue": blast_res["evalue"]
        })

    # Grava o arquivo CSV
    colunas = ["sra", "specie", "len_novo", "len_uni", "pident", "qcovs", "evalue"]
    try:
        with open(args.output, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=colunas)
            writer.writeheader()
            writer.writerows(dados_finais)
        print(f"\nProcesso concluído com sucesso! Resultado salvo em: {args.output}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo CSV: {e}")

if __name__ == "__main__":
    main()