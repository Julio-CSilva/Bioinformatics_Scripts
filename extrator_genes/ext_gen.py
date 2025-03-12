import os

# Diretórios e genes a serem filtrados
dir_fasta = "extrator_genes/fastas"
dir_resultados = "extrator_genes/results"
gen = []  # Deixe vazio para extrair todos os contigs

# Cria o diretório de saída, se não existir
os.makedirs(dir_resultados, exist_ok=True)

def extrair_contigs(arq_input, arq_output, contigs_para_extrair):
    with open(arq_input, "r") as fasta:
        linhas = fasta.readlines()

    contigs = []
    seq_atual = []
    header_atual = None

    # Itera sobre as linhas do arquivo
    for linha in linhas:
        if linha.startswith(">"):  # Novo contig encontrado
            if header_atual and seq_atual:
                contigs.append((header_atual, seq_atual))  # Salva o contig anterior

            header_atual = linha.strip()
            seq_atual = []
        else:
            seq_atual.append(linha.strip())

    # Adiciona o último contig do arquivo
    if header_atual and seq_atual:
        contigs.append((header_atual, seq_atual))

    # Se nenhum gene foi especificado, extrai todos os contigs
    if not contigs_para_extrair:
        for header, seq in contigs:
            nome_gene = header[1:].split()[0]  # Obtém o nome do contig sem ">"
            nome_arquivo = f"{os.path.basename(arq_input).rsplit('.', 1)[0]}_{nome_gene}.fasta"
            caminho_saida = os.path.join(dir_resultados, nome_arquivo)

            with open(caminho_saida, "w") as fasta_out:
                fasta_out.write(header + "\n" + "\n".join(seq) + "\n")
            
            print(f"Contig {nome_gene} extraído e salvo em {nome_arquivo}")

    else:
        for header, seq in contigs:
            for g in contigs_para_extrair:
                if g in header:
                    nome_arquivo = f"{os.path.basename(arq_input).rsplit('.', 1)[0]}_{g}.fasta"
                    caminho_saida = os.path.join(dir_resultados, nome_arquivo)

                    with open(caminho_saida, "w") as fasta_out:
                        fasta_out.write(header + "\n" + "\n".join(seq) + "\n")
                    
                    print(f"Gene {g} extraído e salvo em {nome_arquivo}")

# Percorre todos os arquivos FASTA no diretório especificado
for arquivo in os.listdir(dir_fasta):
    if arquivo.endswith(".fa") or arquivo.endswith(".fasta"):
        path_arq_in = os.path.join(dir_fasta, arquivo)
        extrair_contigs(path_arq_in, dir_resultados, gen)
