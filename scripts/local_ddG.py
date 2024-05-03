#!/usr/bin/env python3
# Analyzing results from local interaction
# Putting all the results in the dictionary
infile = open("binding_DNA_results.txt", "r")
aa_list = []
mutatex_results_Dict = {}
for i, line in enumerate(infile):
    if i == 0:
        for element in line.split()[3:]:
            aa_list.append(element)
    if i >= 1:
        for i, element in enumerate(line.split()[3:]):
            key = line.split()[0] + line.split()[2] + aa_list[i]
            value = float(line.split()[3+i])
            if line.split()[0] != aa_list[i]:
                mutatex_results_Dict[key] = value
infile.close()
#print(mutatex_results_Dict)

# ΔΔG < -1 kcal/mol we could expect the mutation to be stabilizing for the interface and if the ΔΔG > 1 kcal/mol destabilizing
stabilizing_Dict = {}
destabilizing_Dict = {}
for key, value in mutatex_results_Dict.items():
    if value <= -1:
        stabilizing_Dict[key] = value
    elif value >= 1:
        destabilizing_Dict[key] = value

print("if ΔΔG < -1 kcal/mol we could expect the mutation to be stabilizing for the interface and if the ΔΔG > 1 kcal/mol destabilizing")
print("Number of stabilizing mutations is:", str(len(stabilizing_Dict))+",", "which are:")
for element in stabilizing_Dict.items():
    print(element)

# List of all destabilizing mutations
destabilizing_list = list(destabilizing_Dict.keys())
print("\nNumber of destabilizing mutations is:", str(len(destabilizing_Dict))+",", "which are:")
for element in destabilizing_Dict.items():
    print(element)
