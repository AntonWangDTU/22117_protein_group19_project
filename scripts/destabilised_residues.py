#!usr/bin/env python3
import pandas as pd

df2 = pd.read_csv("energies_cabsflex_filtered.csv")
# Define a function to count values greater than 3 in a row
def count_values_greater_than(row, threshold):
    # Count the number of values greater than the threshold in amino acid columns
    count = sum(1 for value in row[4:] if value > threshold)
    return count
# Define threshold
threshold = 3
indices = []

# Calculate indices for each percentage threshold
for percentage in [0.5, 0.6, 0.7, 0.8, 0.9]:
    # Calculate the number of columns required to meet the percentage threshold
    required_columns = int((len(df2.columns) - 4) * percentage)
    indices.append(df2[df2.apply(lambda row: count_values_greater_than(row, threshold), axis=1) >= required_columns].index.tolist())


# Initialize lists to store residues for each percentage threshold
residues_by_threshold = [[] for _ in range(len(indices))]

# Populate residues for each percentage threshold
for i, idx in enumerate(indices):
    residues_by_threshold[i] = df2.loc[idx, 'Residue #'].tolist()

# Print residues for each percentage threshold
for i, percentage in enumerate([50, 60, 70, 80, 90]):
    print(f"Residues for > {percentage}% of values greater than {threshold}:")
    print(residues_by_threshold[i])