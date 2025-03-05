# import csv

# def write_csv_date(data, filename):
#     with open('bible_reading_plan.xlsx', mode='w', newline='') as csv_file:
#         plan_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#         plan_writer.writerow(data[0].keys())
#         for row in plan_writer:
#             plan_writer.writerow(row.values())




#         fieldnames = ['date', 'old_testament', 'new_testament', 'psalm']

# import pandas as pd
# # from data import Bible_Reading_Plan

# # Load your data
# df = pd.read_csv("Bible_Reading_Plan.csv")

# # Replace "/" with "," in the "psalm" column
# df['psalm'] = df['psalm'].str.replace('/', ', ')

# # Fill empty cells with "N/A"
# df['psalm'].fillna("Your choice", inplace=True)

# # Save the cleaned data to a new Excel file
# df.to_excel("cleaned_file.xlsx", index=False, engine='openpyxl')


import pandas as pd

# Load your data
df = pd.read_csv("Bible_Reading_Plan.csv")

# Replace "/" with "," in the "psalm" column
df['psalm'] = df['psalm'].str.replace('/', ', ')

# Fill empty cells with "N/A"
df['psalm'].fillna("N/A", inplace=True)

# Save the cleaned data to a new Excel file using openpyxl engine
df.to_csv("cleaned_file.csv", index=False)
