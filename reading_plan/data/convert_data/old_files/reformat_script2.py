import pandas as pd

# Step 1: Load your data
df = pd.read_csv('bible_readings.csv')

# Step 2: Create a new DataFrame for the reformatted structure
reformatted_data = []

# Step 3: Loop through each row and extract readings
for _, row in df.iterrows():
    date = row['date']
    
    # Add Old Testament readings
    if pd.notna(row['ot_book']) and pd.notna(row['ot_chapter']):
        reformatted_data.append({
            'Date': date,
            'Book': row['ot_book'],
            'Chapter': row['ot_chapter'],
            'Type': 'Old Testament'
        })
    
    # Add New Testament readings
    if pd.notna(row['nt_book']) and pd.notna(row['nt_chapter']):
        reformatted_data.append({
            'Date': date,
            'Book': row['nt_book'],
            'Chapter': row['nt_chapter'],
            'Type': 'New Testament'
        })
    
    # Add Psalm readings
    if pd.notna(row['psalm_book']) and pd.notna(row['psalm_chapter']):
        reformatted_data.append({
            'Date': date,
            'Book': row['psalm_book'],
            'Chapter': row['psalm_chapter'],
            'Type': 'Psalm'
        })

# Step 4: Convert reformatted_data into a DataFrame
reformatted_df = pd.DataFrame(reformatted_data)

# Convert Chapter column to integers, ignoring "Your choice"
reformatted_df['Chapter'] = reformatted_df['Chapter'].apply(
    lambda x: int(x) if pd.notna(x) and isinstance(x, (float, int)) else x
)

# Ensure every day has at least one Psalm entry
all_dates = reformatted_df['Date'].unique()

missing_psalm_entries = []

for date in all_dates:
    psalm_exists = ((reformatted_df['Date'] == date) & (reformatted_df['Type'] == 'Psalm')).any()
    if not psalm_exists:
        missing_psalm_entries.append({
            'Date': date,
            'Book': 'Psalm',
            'Chapter': 'Your choice',
            'Type': 'Psalm'
        })

# Add the missing entries to the DataFrame using pd.concat
missing_psalm_df = pd.DataFrame(missing_psalm_entries)
reformatted_df = pd.concat([reformatted_df, missing_psalm_df], ignore_index=True)

reformatted_df = reformatted_df.sort_values(by='Date')





# Step 5: Save the reformatted data to a new CSV file
reformatted_df.to_csv('reformatted_bible_readings.csv', index=False)

print("Data has been reformatted and saved to 'reformatted_bible_readings.csv'")
