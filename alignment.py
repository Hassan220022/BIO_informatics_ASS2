#!/usr/bin/python3
from Bio.Align.Applications import MuscleCommandline
from Bio import AlignIO

def perform_alignment(input_filepath, output_filepath):
    muscle_cline = MuscleCommandline(input=input_filepath, out=output_filepath)
    stdout, stderr = muscle_cline()
    alignment = AlignIO.read(output_filepath, "fasta")
    print(alignment)

# Set your input and output file paths
input_fasta = "mutated_sequences.fasta"  # This should be the path to your input FASTA file
output_fasta = "aligned_sequences.fasta"  # The path where you want the aligned sequences to be saved

# Perform the alignment
perform_alignment(input_fasta, output_fasta)
