import os

def obter_maior_contig(linhas):
    """
    Analisa as linhas de um arquivo FASTA, identifica todas as contigs
    e retorna a sequência da maior contig baseada no número de bases.
    """
    contigs = []
    cabecalho_atual = ""
    sequencia_atual = []
    
    for linha in linhas:
        linha_limpa = linha.strip()
        if not linha_limpa:
            continue
            
        if linha_limpa.startswith(">"):
            if cabecalho_atual:
                contigs.append((cabecalho_atual, "\n".join(sequencia_atual)))
            cabecalho_atual = linha_limpa
            sequencia_atual = []
        else:
            sequencia_atual.append(linha_limpa)
            
    if cabecalho_atual:
        contigs.append((cabecalho_atual, "\n".join(sequencia_atual)))
        
    if not contigs:
        return None
        
    maior_contig = max(contigs, key=lambda x: len(x[1].replace("\n", "")))
    return maior_contig[1]


dir_path = os.path.join(os.path.dirname(__file__), "fasta")

if not os.path.exists(dir_path):
    print(f"ERRO CRÍTICO: O diretório não foi encontrado -> {dir_path}")
    exit()

arquivos = os.listdir(dir_path)
if not arquivos:
    print("A pasta 'fasta' está vazia.")

for filename in arquivos:
    caminho_arquivo = os.path.join(dir_path, filename)
    
    # Ignora subdiretórios
    if os.path.isdir(caminho_arquivo):
        continue
        
    # 1. Lê o arquivo
    with open(caminho_arquivo, 'r') as file:
        linhas = file.readlines()
        
    # Isola a maior contig
    maior_sequencia = obter_maior_contig(linhas)
    
    if maior_sequencia is None:
        print(f"Ignorado (Vazio ou Inválido): {filename}")
        continue
        
    # 2. Define o novo cabeçalho usando o nome do arquivo
    # os.path.splitext remove a extensão (ex: 'SRA_especies.fa' vira 'SRA_especies')
    nome_sem_extensao = os.path.splitext(filename)[0]
    novo_cabecalho = f">{nome_sem_extensao}\n"
    
    # Sobrescreve o mesmo arquivo (não renomeia o arquivo físico)
    with open(caminho_arquivo, 'w') as file:
        file.write(novo_cabecalho)
        file.write(maior_sequencia + "\n")

    print(f"Processado: {filename} -> Cabeçalho atualizado para '{novo_cabecalho.strip()}'")