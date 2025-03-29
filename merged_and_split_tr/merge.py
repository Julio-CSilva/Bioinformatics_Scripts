import os

# Caminho do diretório principal
file_dir = "merged_and_split_tr/separeted"

# Função para extrair o nome do arquivo
def extract_name(file_name):
    parts = file_name.split("_", 1)  # Divide no primeiro "_"
    return parts[1] if len(parts) > 1 else file_name  # Retorna a parte após o "_", se existir

# Percorre todas as subpastas dentro do diretório
for subfolder in sorted(os.listdir(file_dir), reverse=True):
    subfolder_path = os.path.join(file_dir, subfolder)

    # Verifica se é um diretório
    if os.path.isdir(subfolder_path):
        output_file_path = os.path.join("merged_and_split_tr/merged/", f"{subfolder}.txt")

        # Obtém a lista de arquivos .txt e ordena pelo nome após o código
        txt_files = sorted(
            [f for f in os.listdir(subfolder_path) if f.endswith(".txt")],
            key=extract_name
        )

        with open(output_file_path, "w", encoding="utf-8") as output_file:
            for file_name in txt_files:
                file_path = os.path.join(subfolder_path, file_name)

                with open(file_path, "r", encoding="utf-8") as input_file:
                    output_file.write(input_file.read())
                    output_file.write("\n")

        print(f"Arquivo gerado: {output_file_path}")
    else:
        txt_files = sorted(
            [f for f in os.listdir(file_dir) if f.endswith(".txt")],
            key=extract_name
        )
        output_file_path = os.path.join("merged_and_split_tr/merged/", "merged.txt")
        with open(output_file_path, "w", encoding="utf-8") as output_file:
            for file_name in txt_files:
                file_path = os.path.join(file_dir, file_name)

                with open(file_path, "r", encoding="utf-8") as input_file:
                    output_file.write(input_file.read())
                    output_file.write("\n")
        print(f"Arquivo gerado: {output_file_path}")
        break

