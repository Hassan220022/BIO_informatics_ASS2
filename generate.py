#!/usr/bin/python3
import random

def mutate_protein(sequence, num_mutations):
    protein_letters = 'ACDEFGHIKLMNPQRSTVWY'
    mutated_sequences = []
    
    for _ in range(num_mutations):
        mutated_sequence = ''
        for letter in sequence:
            if random.random() < 0.05:  # Mutation rate of 5%
                mutated_sequence += random.choice(protein_letters)
            else:
                mutated_sequence += letter
        mutated_sequences.append(mutated_sequence)
    
    return mutated_sequences

# Example usage:
sequence = 'MKTAYIAKQRQISFVKSHFSRQLEERLGLIEVQAPILSRVGDGTQDNLSGAEKAVQVKVKAL'
num_mutations = 20
mutated_sequences = mutate_protein(sequence, num_mutations)

for i, seq in enumerate(mutated_sequences, 1):
    print(f'{i}. {seq}')

