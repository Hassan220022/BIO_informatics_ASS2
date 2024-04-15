#!/usr/bin/python3
import random

def mutate_protein(sequence, num_mutations):
    protein_letters = 'ACDEFGHIKLMNPQRSTVWY'
    mutated_sequences = []
    
    for _ in range(num_mutations):
        mutated_sequence = list(sequence)  # Convert the sequence to a list to allow easy modification
        for i in range(len(sequence)):
            if random.random() < 0.05:  # Mutation rate of 5%
                mutated_sequence[i] = random.choice(protein_letters)
        mutated_sequences.append(''.join(mutated_sequence))
    
    return mutated_sequences

# Read sequences from Input.txt
sequences = []
with open("Input.txt", "r") as f:
    lines = f.readlines()
    sequence = ''
    for line in lines:
        if not line.startswith(">"):
            sequence += line.strip()
    sequences.append(sequence)

# Mutate each sequence and save to a text file
num_mutations = 20
mutated_sequences = []
for seq in sequences:
    mutated_seq = mutate_protein(seq, num_mutations)
    mutated_seq = [mut_seq[:len(seq)] for mut_seq in mutated_seq]  # Truncate mutated sequences to the length of the input sequence
    mutated_sequences.extend(mutated_seq)

# Save mutated sequences to a text file in FASTA format
txt_file = "mutated_sequences.fasta"
with open(txt_file, "w") as f:
    for i, seq in enumerate(mutated_sequences, 1):
        f.write(f">{i}\n{seq}\n")

print(f"Mutated sequences saved to {txt_file}")
