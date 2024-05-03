#!/usr/bin/env python3
# amino acids dictionary
aa_Dict = {
    "Ala": "A",
    "Arg": "R",
    "Asn": "N",
    "Asp": "D",
    "Cys": "C",
    "Gln": "Q",
    "Glu": "E",
    "Gly": "G",
    "His": "H",
    "Ile": "I",
    "Leu": "L",
    "Lys": "K",
    "Met": "M",
    "Phe": "F",
    "Pro": "P",
    "Ser": "S",
    "Thr": "T",
    "Trp": "W",
    "Tyr": "Y",
    "Val": "V",
    "Ter": "termination",
    "fs": "frame shift"
}

# Positions used for local interaction analysis (close proximity to DNA)
mutatex_positions= [870, 871, 872, 873, 896, 897, 898, 899, 919, 920, 921, 927, 946, 947, 948, 968, 994, 996, 1000, 1003, 1004, 1005, 1007, 1008, 1110, 1112, 1113, 1120, 1121, 1122, 1123, 1139, 1162, 1163, 1164, 1165, 1166, 1168, 1169, 1170]


# Reading file downloaded from from ClinVar repository consisting pathogenic mutations of BLM only
import re
infile = open("pathogenic_BLM.txt", "r")
mutations_list = []
mutations_positions = []
for i, line in enumerate(infile):
    if re.match(r'\(p\.[A-Za-z]+\d+[A-Za-z]+\)', line.split()[1]) and re.search(r'Bloom', line):
        #print(line)
        mutation = line.split()[1][3:-1]
        position = re.findall(r'\d+', line.split()[1])
        mutations_positions.append(position[0])
        mutations_list.append(mutation)
#print(mutations_list)
infile.close()

# Filtering pathogenic mutations to leave only those that are around the region of DNA binding 
patho_mutations_filtered = []
patho_positions = []
for mutation in mutations_list:
    position = re.search(r'\d+', mutation)
    if position:
        position = int(position.group())
        if 870 <= position <= 1170:
            patho_mutations_filtered.append(mutation)
            patho_positions.append(position)
#print(patho_mutations_filtered)
#print(patho_positions)

# How many pathogenic positions were used for local interaction analysis (overlap of 2 lists)?
overlap = set(mutatex_positions) & set(patho_positions)
print("Pathogenic positions according to ClinVar in the region of in of interest (region interacting with DNA duplex) are:")
for position in overlap:
    print(position)

# All pathogenic mutations are either due to frameshifts or the insertion of an early termination codon.
"""
994 - 'Thr994fs'
1123 - 'Ser1123fs'
899 - 'Arg899Ter'
1003 - 'Arg1003Ter'
1004 - 'Leu1004fs'
1166 - 'Gln1166Ter'
1170 - 'Tyr1170Ter'
1139 - 'Arg1139Ter'
"""
