#!/usr/bin/env python3
import matplotlib.pyplot as plt

# List of positions and counts
positions_counts = [
    (870, 0), (873, 0), (919, 0), (927, 0), (968, 0), (994, 0), (1003, 0), 
    (1007, 0), (1113, 0), (1120, 0), (1121, 0), (1122, 0), (1123, 0), 
    (1139, 0), (1163, 0), (1165, 0), (1170, 0), (899, 1), (920, 1), 
    (1169, 1), (1112, 2), (1166, 2), (872, 3), (896, 3), (1005, 3), 
    (921, 4), (898, 5), (996, 5), (1162, 5), (871, 6), (947, 7), 
    (897, 8), (1164, 11), (1168, 11), (948, 12), (1004, 16), 
    (1008, 16), (946, 18), (1110, 18), (1000, 19)
]

# Sort positions_counts based on position values
positions_counts.sort(key=lambda x: x[0])

# Extract positions and counts separately
positions = [str(item[0]) for item in positions_counts]
counts = [item[1] for item in positions_counts]

# Plot for all positions
plt.figure(figsize=(14, 6))
bars = plt.bar(positions, counts)
plt.xlabel('Positions', fontsize=14)
plt.ylabel('Number of destabilizing mutations', fontsize=14)
plt.title('Number of destabilizing mutations for each position', fontsize=16)
plt.xticks(rotation=45, ha='right', fontsize=8)
plt.yticks(range(int(max(counts)) + 1))
plt.tight_layout()

plt.show()
