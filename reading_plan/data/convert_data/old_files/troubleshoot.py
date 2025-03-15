import csv
from collections import defaultdict

# Input file
input_file = 'reformatted_bible_readings.csv'

# Dictionary to store row counts by date
date_counts = defaultdict(int)

# Read the CSV and count rows for each date
with open(input_file, 'r') as infile:
    reader = csv.reader(infile)
    next(reader)  # Skip header row
    
    for row in reader:
        date = row[0]  # Assuming 'date' is the first column (index 0)
        date_counts[date] += 1

# Print the counts
for date, count in date_counts.items():
    print(f"{date}: {count} rows")
