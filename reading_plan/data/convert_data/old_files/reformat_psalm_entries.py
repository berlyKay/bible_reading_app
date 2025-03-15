import csv

# Input and output files
input_file = 'reformatted_bible_readings.csv'
output_file = 'bible_readings_cleaned.csv'

# Process the file
with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    # Write the header row
    header = next(reader)
    writer.writerow(header)
    
    for row in reader:
        book = row[1]  # Assuming "Book" is the second column (index 1)
        print(book.strip())
        
        # Check if the "Book" field is numeric
        if book.strip().isdigit():
            # Split multiple chapters (e.g., "106," "122") into separate rows
            chapters = row[4].split(",")  # Assuming chapters are in column 5 (index 4)
            for chapter in chapters:
                clean_row = row[:]
                clean_row[4] = chapter.strip()  # Replace with individual chapter
                writer.writerow(clean_row)
        else:
            # If not numeric, just write the row as-is
            writer.writerow(row)
