#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script para comparar pares de arquivos FASTA de dois diretórios.

Este script percorre os arquivos no primeiro diretório, encontra os arquivos
de mesmo nome no segundo diretório e compara as sequências contidas neles.

Primeiro, ele faz uma verificação de identidade exata. Se as sequências não
forem idênticas, ele executa um alinhamento local usando blastn para calcular
a porcentagem de identidade e a cobertura.
"""

import os
import shutil
import argparse
import io
from Bio.SeqIO import read as SeqIO_read
from Bio.Blast.Applications import NcbiblastnCommandline
from Bio.Blast import NCBIXML

def comparar_sequencias(arquivo_query, arquivo_subject):
    """
    Compara duas sequências de arquivos FASTA.

    Args:
        arquivo_query (str): Caminho para o arquivo FASTA da query.
        arquivo_subject (str): Caminho para o arquivo FASTA do subject (alvo).

    Returns:
        dict: Um dicionário contendo os resultados da comparação.
    """
    try:
        # 1. Tenta ler as sequências dos arquivos
        seq_query = SeqIO_read(arquivo_query, "fasta")
        seq_subject = SeqIO_read(arquivo_subject, "fasta")

        # 2. Se não forem idênticas, executa o BLAST
        # O comando será: blastn -query <arquivo_query> -subject <arquivo_subject> -outfmt 5
        blastn_cline = NcbiblastnCommandline(
            query=arquivo_query,
            subject=arquivo_subject,
            outfmt=5  # Formato de saída XML
        )

        stdout, stderr = blastn_cline()

        # 3. Analisa o resultado XML do BLAST
        blast_record = NCBIXML.read(io.StringIO(stdout))

        # Se não houver alinhamentos, não há similaridade significativa
        if not blast_record.alignments:
            return {
                "status": "sem alinhamento BLAST",
                "identidade": 0.0,
                "cobertura": 0.0
            }

        # Pega o primeiro e melhor alinhamento (High-Scoring Pair - HSP)
        hsp = blast_record.alignments[0].hsps[0]

        # Calcula a porcentagem de identidade e cobertura
        identidade = (hsp.identities / hsp.align_length) * 100
        cobertura_query = (hsp.align_length / len(seq_query.seq)) * 100

        return {
            "status": "Match BLAST",
            "identidade": identidade,
            "cobertura": cobertura_query,
            "e_value": hsp.expect,
            "tamanho_query": len(seq_query.seq),
            "tamanho_subject": len(seq_subject.seq)
        }

    except FileNotFoundError:
        return {"status": "ERRO", "mensagem": f"Arquivo não encontrado: {arquivo_query} ou {arquivo_subject}"}
    except ValueError as e:
        # Erro comum se o arquivo FASTA estiver vazio ou mal formatado
        return {"status": "ERRO", "mensagem": f"Erro ao ler o FASTA: {e}"}
    except Exception as e:
        # Captura outros erros, como o BLAST+ não estar instalado
        return {"status": "ERRO", "mensagem": f"Ocorreu um erro inesperado: {e}"}

def main():
    parser = argparse.ArgumentParser(
        description="Compara arquivos FASTA de mesmo nome em dois diretórios usando BLAST."
    )
    parser.add_argument("dir1", help="O primeiro diretório (contém as queries).")
    parser.add_argument("dir2", help="O segundo diretório (contém os subjects/alvos).")

    args = parser.parse_args()

    if not os.path.isdir(args.dir1):
        print(f"Erro: O diretório '{args.dir1}' não existe.")
        return
    if not os.path.isdir(args.dir2):
        print(f"Erro: O diretório '{args.dir2}' não existe.")
        return

    # Lista arquivos no primeiro diretório
    arquivos_dir1 = [f for f in os.listdir(args.dir1) if os.path.isfile(os.path.join(args.dir1, f))]

    if not arquivos_dir1:
        print(f"Nenhum arquivo encontrado no diretório '{args.dir1}'.")
        return

    print("-" * 60)
    print(f"Comparando arquivos de '{args.dir1}' com '{args.dir2}'")
    print("-" * 60)

    for nome_arquivo in sorted(arquivos_dir1):
        caminho_query = os.path.join(args.dir1, nome_arquivo)
        caminho_subject = os.path.join(args.dir2, nome_arquivo)

        print(f"\nComparando: {nome_arquivo}")

        if not os.path.exists(caminho_subject):
            print(f"  -> AVISO: Arquivo correspondente não encontrado em '{args.dir2}'. Pulando.")
            continue

        resultado = comparar_sequencias(caminho_query, caminho_subject)

        if resultado["status"] == "ERRO":
            print(f"  -> ERRO: {resultado['mensagem']}")
        elif resultado["identidade"] >= 99.9:
            print(f"  -> Status: {resultado['status']}")
            if "identidade" in resultado:
                print(f"     Similaridade (BLAST): {resultado['identidade']:.2f}%")
                print(f"     Cobertura da Query:   {resultado['cobertura']:.2f}%")
                print(f"     E-value:              {resultado['e_value']:.2e}")
            #shutil.move(caminho_subject, os.path.join(os.path.dirname(__file__), "similar/fastaCircularized"))
            #shutil.move(caminho_query, os.path.join(os.path.dirname(__file__), "similar/fasta"))
        else:
            print(f"  -> Status: {resultado['status']}")
            if "identidade" in resultado:
                print(f"     Similaridade (BLAST): {resultado['identidade']:.2f}%")
                print(f"     Cobertura da Query:   {resultado['cobertura']:.2f}%")
                print(f"     E-value:              {resultado['e_value']:.2e}")

    print("\n" + "-" * 60)
    print("Comparação concluída.")
    print("-" * 60)

if __name__ == "__main__":
    main()