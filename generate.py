#!/usr/bin/python3
import random
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

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

# Create a PDF file and draw the mutated sequences on it
pdf_file = "mutated_sequences.pdf"
c = canvas.Canvas(pdf_file, pagesize=letter)
c.setFont("Helvetica", 12)

for i, seq in enumerate(mutated_sequences, 1):
    c.drawString(100, 800 - i * 20, f"{i}. {seq}")

c.save()

print(f"Mutated sequences saved to {pdf_file}")

