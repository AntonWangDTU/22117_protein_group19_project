#!/bin/env python3 

import re

def convert_amino_acid(abbr):
    amino_acids = {
        'Ala': 'A', 'Arg': 'R', 'Asn': 'N', 'Asp': 'D', 'Cys': 'C',
        'Gln': 'Q', 'Glu': 'E', 'Gly': 'G', 'His': 'H', 'Ile': 'I',
        'Leu': 'L', 'Lys': 'K', 'Met': 'M', 'Phe': 'F', 'Pro': 'P',
        'Ser': 'S', 'Thr': 'T', 'Trp': 'W', 'Tyr': 'Y', 'Val': 'V',
        'Ter': '*'
    }
    return amino_acids.get(abbr, abbr)

def extract_positions(line):
    matches = re.findall(r'p\.([A-Za-z]{3})(\d+)(?:([A-Za-z]{3})(\d+))?(?:fs)?', line)
    positions = []
    for match in matches:
        abbr1, pos1, abbr2, pos2 = match
        if abbr2 and pos2:
            pos1_int = int(pos1)
            pos2_int = int(pos2)
            if 640 <= pos1_int <= 1300:
                positions.append(f'{convert_amino_acid(abbr1)}{pos1_int}')
            if 640 <= pos2_int <= 1300:
                positions.append(f'{convert_amino_acid(abbr2)}{pos2_int}')
        else:
            pos1_int = int(pos1)
            if 640 <= pos1_int <= 1300:
                positions.append(f'{convert_amino_acid(abbr1)}{pos1_int}')
    return positions

# Read the file and process each line
output_positions = []
with open('clinvar_result.txt', 'r') as file:
    for line in file:
        if re.search(r"Bloom syndrome", line):
            positions = extract_positions(line)
            if positions:
                output_positions.extend(positions)

# Write the positions to a file
with open('positions.txt', 'w') as output_file:
    for position in output_positions:
        output_file.write(position + '\n')