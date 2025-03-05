import csv

from reading_plan.models import ReadingPlan

with open('./reading_plan/data/Bible_Reading_Plan.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        reading = ReadingPlan(
            date=row[0],
            old_testament=row[2],
            new_testament=row[3],
            psalm=row[4]
        )
        reading.save()  # Saves it to the database
