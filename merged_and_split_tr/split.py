import os
import re

input_directory = "merged_and_split_tr/files_tr"
output_directory = "merged_and_split_tr/separated"

def split_txt_files(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if not os.path.exists(filename):
            name_dir = filename.split(".")[0]
            os.makedirs(os.path.join(output_dir, name_dir))

        if filename.endswith(".txt"):
            input_path = os.path.join(input_dir, filename)
            with open(input_path, "r", encoding="utf-8") as file:
                content = file.read()
            
            blocks = re.split(r'>(\S+)', content)[1:]  # Divide pelo '>' e mantém os nomes
            
            for i in range(0, len(blocks), 2):
                file_name = blocks[i].strip()
                data = blocks[i + 1].strip()
                output_path = os.path.join(f"{output_dir}/{name_dir}", f"{file_name}.txt")
                
                with open(output_path, "w", encoding="utf-8") as out_file:
                    out_file.write(f">{file_name}\n{data}\n")

name_dir = ""
split_txt_files(input_directory, output_directory)
