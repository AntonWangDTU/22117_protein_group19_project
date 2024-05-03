#!usr/bin/env python3
import pandas as pd

df = pd.read_csv('energies.csv')
#Create an empty DataFrame to store the values, 'Residue #', and 'WT residue type' columns
result_df = pd.DataFrame(columns=['Residue #', 'WT residue type', 'Value'])

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    # Extract the value for the amino acid in the corresponding column
    value_for_amino_acid = row[index]
    # Append the 'Residue #', 'WT residue type', and value to the DataFrame
    result_df = result_df.append({'Residue #': row['Residue #'], 'WT residue type': index, 'Value': value_for_amino_acid}, ignore_index=True)

# rigth the data frame to a file
result_df.to_csv('self_scan_before_cabsflex.csv',index=False)
# Print the resulting DataFrame
print(result_df)