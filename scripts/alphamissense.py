#!/usr/bin/env python3
import re

with open("alphamissense_P54132.tsv","r") as infile, open("variants.txt","w") as outfile:
    infile.readline()
    for line in infile:
        searchline = line.split()
        #search for the region 600-1299
        match = re.search(r"[A-Z][6-9]\d\d[A-Z]|[A-Z][1][0-2]\d{2}[A-Z]",searchline[1])
        if match:
            print(line, file= outfile, end="")

with open("alphamissense_P54132.tsv","r") as infile, open("variants_pathogenic.txt","w") as outfile:
    infile.readline()
    for line in infile:
        searchline = line.split()
        # search for the regions 600-1299
        match = re.search(r"[A-Z][6-9]\d\d[A-Z]|[A-Z][1][0-2]\d{2}[A-Z]",searchline[1])
        
        if match and "pathogenic"==searchline[3]:
            print(line, file= outfile, end="")