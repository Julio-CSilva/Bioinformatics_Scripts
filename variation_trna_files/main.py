import os
from collections import defaultdict
from pathlib import Path as path

dir_files = "variation_trna_files/trna_files"  # Substitua pelo caminho real


def species_group(dir_files):
    specie_group = defaultdict(list)
    
    # Agrupar pastas pelo segundo nome
    for pasta in os.listdir(dir_files):
        partes = pasta.split(" - ") or pasta.split("_")
        if len(partes) > 1:
            codigo, especie = partes[0], partes[1]
            specie_group[especie].append((codigo, pasta))
    return specie_group

def variation_files(groups):
        for code, past_name in groups:
            for i in range(len(groups)-1):
                variation1 = set(os.listdir(os.path.join(dir_files, past_name))) - set(os.listdir(os.path.join(dir_files, groups[i+1][1])))
                variation2 = set(os.listdir(os.path.join(dir_files, groups[i+1][1]))) - set(os.listdir(os.path.join(dir_files, past_name)))
                variation_all = variation1.union(variation2)

                if variation_all:
                    with open("variation_trna_files/result_variation.txt", "a") as file:
                        file.write(f"[{past_name}] x [{groups[i+1][1]}]\t{variation_all}\n")

dir_files = path(dir_files).absolute()
groups = species_group(dir_files)
print(groups)
for specie, pastas in groups.items():
    variation_files(pastas)

