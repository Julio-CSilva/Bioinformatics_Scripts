import os

# Diretório contendo os arquivos .fa e/ou .fasta
directory = "dir_files"
# Arquivo de saída .csv
output_file = "analysis_contigs.csv"

# Função para calcular a porcentagem de A e T na sequência
def calcular_porcentagem_AT(sequencia):
    sequencia = sequencia.upper()
    total = len(sequencia.replace('\n', ''))
    count_AT = sequencia.count('A') + sequencia.count('T')
    return (count_AT / total) * 100 if total > 0 else 0

# Função para calcular o AT skew na sequência
def calcular_AT_skew(sequencia):
    count_A = sequencia.count('A')
    count_T = sequencia.count('T')
    total_AT = count_A + count_T
    return (count_A - count_T) / total_AT if total_AT != 0 else 0

# Função para salvar os resultados de cada contig no arquivo .csv
def results(sequence, filename, contig, char_count):
    pct_AT = calcular_porcentagem_AT(sequence)
    skew_AT = calcular_AT_skew(sequence)
    out_f.write(f"{filename},{contig},{char_count},{pct_AT:.2f},{(100-pct_AT):.2f},{skew_AT:.2f}\n")

with open(output_file, "w") as out_f:
    # Escrever o cabeçalho do .csv
    out_f.write("File,Contigs,Amount,%AT,%CG,AT Skew\n")
    
    for filename in os.listdir(directory):
        if filename.endswith(".fa") or filename.endswith(".fasta"):
            filepath = os.path.join(directory, filename)
            
            count_contig = 1
            char_count = 0
            sequence = ""
            contig = ""
            with open(filepath, "r") as f:
                for line in f:
                    line = line.strip()
                    if line[0] == ">" and count_contig == 1:
                        if char_count > 0:
                            results(sequence, filename, contig, char_count)
                        contig = line
                        count_contig += 1
                    elif (line[0] == ">" and count_contig >= 2):
                        results(sequence, filename, contig, char_count)
                        contig = line
                        char_count = 0
                        sequence = ""
                    else:
                        char_count += len(line)
                        sequence += line
                results(sequence, filename, contig, char_count)

print(f"Resultados salvos em {output_file}")