#!/usr/bin/env python3
import re

# Reading alphamissense results
infile = open("alphamissense_P54132.tsv", "r")
alphamissense_list = []
destabilizing_list = ['P871G', 'P871W', 'P871S', 'P871Y', 'P871N', 'P871E', 'K872G', 'K872P', 'K872T', 'L896W', 'L896Y', 'L896R', 'S897L', 'S897F', 'S897W', 'S897T', 'S897Y', 'S897K', 'S897R', 'S897H', 'R898F', 'R898W', 'R898P', 'R898Y', 'R898D', 'R899P', 'A920P', 'G921V', 'G921I', 'G921P', 'G921T', 'T946G', 'T946A', 'T946V', 'T946L', 'T946I', 'T946M', 'T946F', 'T946W', 'T946P', 'T946C', 'T946Y', 'T946N', 'T946Q', 'T946D', 'T946E', 'T946K', 'T946R', 'T946H', 'I947G', 'I947A', 'I947S', 'I947N', 'I947D', 'I947E', 'I947H', 'A948L', 'A948M', 'A948F', 'A948W', 'A948P', 'A948Y', 'A948N', 'A948D', 'A948E', 'A948K', 'A948R', 'A948H', 'H996P', 'H996D', 'H996E', 'H996K', 'H996R', 'R1000G', 'R1000A', 'R1000V', 'R1000L', 'R1000I', 'R1000M', 'R1000F', 'R1000W', 'R1000P', 'R1000S', 'R1000T', 'R1000C', 'R1000Y', 'R1000N', 'R1000Q', 'R1000D', 'R1000E', 'R1000K', 'R1000H', 'L1004G', 'L1004A', 'L1004F', 'L1004W', 'L1004P', 'L1004S', 'L1004T', 'L1004C', 'L1004Y', 'L1004N', 'L1004Q', 'L1004D', 'L1004E', 'L1004K', 'L1004R', 'L1004H', 'I1005W', 'I1005D', 'I1005H', 'E1008G', 'E1008A', 'E1008V', 'E1008L', 'E1008I', 'E1008M', 'E1008F', 'E1008W', 'E1008P', 'E1008S', 'E1008T', 'E1008C', 'E1008Y', 'E1008N', 'E1008R', 'E1008H', 'T1110G', 'T1110A', 'T1110V', 'T1110L', 'T1110I', 'T1110M', 'T1110F', 'T1110W', 'T1110P', 'T1110C', 'T1110Y', 'T1110N', 'T1110Q', 'T1110D', 'T1110E', 'T1110K', 'T1110R', 'T1110H', 'N1112D', 'N1112E', 'N1162Y', 'N1162E', 'N1162K', 'N1162R', 'N1162H', 'N1164G', 'N1164A', 'N1164I', 'N1164F', 'N1164W', 'N1164P', 'N1164S', 'N1164Y', 'N1164Q', 'N1164E', 'N1164H', 'Q1166T', 'Q1166E', 'I1168G', 'I1168A', 'I1168W', 'I1168P', 'I1168S', 'I1168T', 'I1168C', 'I1168N', 'I1168Q', 'I1168D', 'I1168E', 'A1169R']
positions = [870, 871, 872, 873, 896, 897, 898, 899, 919, 920, 921, 927, 946, 947, 948, 968, 994, 996, 1000, 1003, 1004, 1005, 1007, 1008, 1110, 1112, 1113, 1120, 1121, 1122, 1123, 1139, 1162, 1163, 1164, 1165, 1166, 1168, 1169, 1170]
for i, line in enumerate(infile):
    if i >= 1:
        position = int(re.search(r'\d+', line.split()[1]).group())
        if position in positions and line.split()[3] == "pathogenic":
            alphamissense_list.append(line.split()[1])
infile.close()
#print(alphamissense_list)
#print(destabilizing_list)

# Find overlap with alphamissense pathogenic mutations
overlap_patho = set(alphamissense_list) & set(destabilizing_list)
print("Overlap between alphamissense 'pathogenic' mutations and detstabilizing mutations found after running mutateX:")
for element in overlap_patho:
    print(element)
