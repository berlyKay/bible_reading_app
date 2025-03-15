from django.core.management.base import BaseCommand
import csv
from reading_plan.models import ReadingPlan

class Command(BaseCommand):
    help = "Import reading plan data from a CSV file"

    def handle(self, *args, **kwargs):
        file_path = './reading_plan/data/bible_reading_plan.csv'  # Ensure this is the correct file

        try:
            with open(file_path, 'r') as file:
                csv_reader = csv.reader(file)
                next(csv_reader)  # Skip header row

                for row in csv_reader:
                    # Debugging: Print each row before processing
                    print(f"Row length: {len(row)} - Data: {row}")

                    # Ensure the row has exactly 7 columns before inserting
                    if len(row) < 7:
                        print(f"Skipping malformed row: {row}")
                        continue  # Skip this row

                    # Create and save a ReadingPlan entry
                    reading = ReadingPlan(
                        date=row[0],
                        ot_book=row[1],
                        ot_chapter=row[2],
                        nt_book=row[3],
                        nt_chapter=row[4],
                        psalm_book=row[5],
                        psalm_chapter=row[6]
                    )
                    reading.save()  # Explicitly save to the database

                    # Debugging: Confirm insertion
                    print(f"✅ Inserted into DB: {reading}")

            self.stdout.write(self.style.SUCCESS("Successfully imported reading plan!"))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error: {e}"))
