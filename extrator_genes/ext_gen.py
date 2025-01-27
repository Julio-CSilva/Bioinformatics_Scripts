import os

# Defina o diretório onde estão os arquivos FASTA
dir_fasta = "fastas"
# Defina o gene/genes que será(ão) extraido dos arquivos FASTA
gen = ["COXI","COXII","COXIII"]
# Defina o diretório onde será colocado os arquivos resultados
dir_resultados = "results"	

def filtrar_gens(arq_input, arq_output, gen):
    with open(arq_input, "r+") as fasta, open(arq_output, "w") as fasta_out:
        linhas = fasta.readlines()
        fasta.seek(0)
        for i in range(len(linhas)):
            if linhas[i].startswith(">"+g):
                inicio = i
                for j in range(i+1, len(linhas)):
                    if linhas[j].startswith(">"):
                        fim = j
                        break
                fasta_out.writelines(linhas[inicio:fim])
                break

# Percorra todos os arquivos FASTA no diretório especificado
for arquivo in os.listdir(dir_fasta):
    if arquivo.endswith(".fa") or arquivo.endswith(".fasta"):
        path_arq_in = os.path.join(dir_fasta, arquivo)
        
        for g in gen:
            new_name = arquivo.rsplit(".", 1)[0] + "_" + g +".fasta"
            path_arq_out = os.path.join(dir_resultados, new_name)
            filtrar_gens(path_arq_in, path_arq_out, g)
            print(f"Gene {g} extraído do arquivo {arquivo} e salvo em {new_name}")
