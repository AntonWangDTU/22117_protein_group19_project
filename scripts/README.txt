
This readme describes the scripts in this folder. The scripts  is used throughout the project.


#####stability_code.ipyn#####
This is a jupyter notebook where the code used for the "MutateX_stability" section is provided. The code
must be viewed in jupyter notebook. 


#####find_pos_script.py#####

This script finds positions from the data derived from clinvar, the scripts outputs into a file "positions.txt". 
The output are the positions that are in the clinvar data, but also in the residue range of our structure.
Running: ./find_pos_script.py <clinvar_result.csv>

#####alphamissense.py#####

This script opens the tsv output file from the Alphamissense tool and keep only the region of the sequence of the studied protein structure(4O3M).
Then it write the mining to a new file, here named "variants.txt". 
There is also the capability to wirte only the pathogenic mutations for the region.
Running: ./alphamissense.py 

####self_scan_check.py#####

This script extracts the values from the "energies.csv" files which correspond to the substitution of each residue with itself
Running : ./self_scan_check.py

#####destabilised_residues.py#####

This script extracts the residues with destabilised mutations over a cut-off for only the 13 residues that have shown extreme ddgs 
in the mutateX stability of static structure.
Running: ./destabilsed_residues.py
