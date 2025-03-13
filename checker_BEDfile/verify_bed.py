import os
import shutil

directory_bedFiles = "beds" # Diretório com os arquivos .bed
verified_dir = "verified" # Diretório onde serão movidos os arquivos .bed verificados

def read_bed_file(file_path):
    """Lê um arquivo .bed, altera a 1ª coluna para o nome do arquivo e verifica o Dloop."""
    genes_found = set()
    line_count = 0

    # Obtém o nome do arquivo sem extensão
    file_name = os.path.splitext(os.path.basename(file_path))[0]

    # Lê todas as linhas do arquivo
    with open(file_path, 'r') as f:
        linhas = f.readlines()

    # Reabre o arquivo para sobrescrever com as alterações
    with open(file_path, 'w') as f:
        for line in linhas:
            line_count += 1
            columns = line.strip().split('\t')
            
            if len(columns) == 6:
                # Altera a primeira coluna para o nome do arquivo
                columns[0] = file_name  

                # Adiciona gene à lista de encontrados
                genes_found.add(columns[3])

                # Modifica o '-' para '+' caso seja Dloop
                if columns[3] == "Dloop" and columns[5] == "-":
                    columns[5] = "+"

            # Reescreve a linha modificada
            f.write('\t'.join(columns) + '\n')

    return genes_found, line_count

def check_genes_in_bed(directory_bedFiles):
    """Verifica se todos os genes esperados estão presentes nos arquivos .bed do diretório e se têm 38 linhas."""
    expected_genes = {
        "rrnS", "rrnL",
        "nad2", "nad1", "cox1", "cox2", "atp8", "atp6", "cox3", "nad3", "nad4l", "nad4",
        "nad5", "nad6", "cob",
        "trnF(gaa)", "trnV(tac)", "trnL2(taa)", "trnI(gat)", "trnQ(ttg)", "trnM(cat)",
        "trnW(tca)", "trnA(tgc)", "trnN(gtt)", "trnC(gca)", "trnY(gta)", "trnS2(tga)", "trnD(gtc)", "trnK(ttt)", "trnG(tcc)", "trnR(tcg)", "trnH(gtg)", "trnS1(gct)", "trnL1(tag)", "trnE(ttc)", "trnT(tgt)", "trnP(tgg)",
        "Dloop"
    }
    
    results = {}
    os.makedirs(verified_dir, exist_ok=True)
    
    for bedfile in os.listdir(directory_bedFiles):
        if bedfile.endswith(".bed"):
            file_path = os.path.join(directory_bedFiles, bedfile)
            found_genes, line_count = read_bed_file(file_path)
            missing_genes = expected_genes - found_genes
            
            if "Dloop" in missing_genes:
                addicion_dloop(bedfile)
                line_count += 1
                missing_genes.remove("Dloop")

            if "trnV(cac)" in found_genes and "trnV(tac)" in missing_genes:
                missing_genes.remove("trnV(tac)")

            is_complete = (line_count == 38)
            if is_complete and not missing_genes:
                shutil.move(file_path, os.path.join(verified_dir, bedfile))
            
            results[bedfile] = {"missing_genes": missing_genes, "is_complete": is_complete, "contained_genes": found_genes}
    
    return results

def addicion_dloop(file_bed):
    last_position = 0
    last_value = ""
    name_file = file_bed.split(".")[0]
    with open(directory_bedFiles+"/"+file_bed, 'r') as f:
        for line in f:
            columns = line.strip().split('\t')
            last_position = int(columns[2])
            last_value = columns[4]
    

    with open(directory_bedFiles+"/"+file_bed, 'a') as f:
        f.write(f"{name_file}\t{last_position+1}\t{18892}\tDloop\t{last_value}\t{"+"}\n")

def main():
    if not os.path.isdir(directory_bedFiles):
        print("O diretório especificado não existe.")
        return
    
    results = check_genes_in_bed(directory_bedFiles)
    
    for file, data in results.items():
        split_gens = []
        missing = data["missing_genes"]
        genes = data["contained_genes"]
        complete = data["is_complete"]

        for gene in missing:
            if gene+"_0" in genes:
                split_gens.append(gene)
        for gene in split_gens:
            missing.remove(gene)

        if missing and split_gens:
            print(f"Arquivo: {file} - Genes ausentes: {', '.join(missing)} - Genes splitados: {', '.join(split_gens)}")
        elif missing:
            print(f"Arquivo: {file} - Genes ausentes: {', '.join(missing)}")
        elif split_gens:
            print(f"Arquivo: {file} - Genes splitados: {', '.join(split_gens)}")
        else:
            continue

if __name__ == "__main__":
    main()
