import os

dir_path = os.path.join(os.path.dirname(__file__), "fasta")
dict_path = os.path.join(os.path.dirname(__file__), "dict_species_orderby.txt") # Path to the dictionary file

list = []
with open(dict_path, "r") as file:
    for line in file:
        list.append(line.strip().split(":"))

dict_species = dict(list)

for filename in os.listdir(dir_path):
    partes = filename.split("_")
    
    with open (os.path.join(dir_path, filename), 'r+') as file:
        lines = file.readlines()
        if lines[0].startswith(">"):
            # Remove the ">" character and split the line by "_"
            lines[0] = f">{partes[3]}_{dict_species[partes[3]]}\n"

        file.seek(0)
        file.writelines(lines)
        file.truncate()

    new_name = f"{partes[3]}_{dict_species[partes[3]]}.fasta"
    old_path = os.path.join(dir_path, filename)
    new_path = os.path.join(dir_path, new_name)
    os.rename(old_path, new_path)
    print(f"Renomeado: {filename} -> {new_name}")
