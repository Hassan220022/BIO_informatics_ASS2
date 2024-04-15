#!/usr/bin/python3
from BioPython import pairwise2
from itertools import combinations
import re

# Read sequences from the file
sequences = []
current_sequence = ''
with open('mutated_sequences.fasta', 'r') as file:
    for line in file:
        line = line.strip()
        if line.startswith('>'):
            if current_sequence:
                # Remove non-standard characters (anything other than A, T, C, G)
                current_sequence = re.sub('[^ATCG]', '', current_sequence.upper())
                sequences.append(current_sequence)
                current_sequence = ''
        else:
            current_sequence += line
    # Append the last sequence
    if current_sequence:
        current_sequence = re.sub('[^ATCG]', '', current_sequence.upper())
        sequences.append(current_sequence)

# Define a function to calculate percentage identity
def calculate_percentage_identity(seq1, seq2):
    alignment = pairwise2.align.globalxx(seq1, seq2, score_only=True)
    length = max(len(seq1), len(seq2))
    identity = alignment / length * 100
    return identity

# Find pairs with at least 30% identity
pairs_with_30_percent_identity = []
for pair in combinations(sequences, 2):
    identity = calculate_percentage_identity(pair[0], pair[1])
    if identity >= 30:
        pairs_with_30_percent_identity.append(identity)

# Print the percentages
print("Percentages of identity for pairs with at least 30% identity:")
if not pairs_with_30_percent_identity:
    print("No pairs with at least 30% identity found.")
else:
    for identity in pairs_with_30_percent_identity:
        print(f"{identity:.2f}%")
