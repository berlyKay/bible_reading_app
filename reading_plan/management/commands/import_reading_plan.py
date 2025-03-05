from django.core.management.base import BaseCommand
import csv
from reading_plan.models import ReadingPlan

class Command(BaseCommand):
    help = "Import reading plan data from a CSV file"

    def handle(self, *args, **kwargs):
        file_path = './reading_plan/data/Bible_Reading_Plan.csv'

        try:
            with open(file_path, 'r') as file:
                csv_reader = csv.reader(file)
                next(csv_reader)  # Skip header row

                for row in csv_reader:
                    print(f"Inserting: {row}")  # Debugging output
                    ReadingPlan.objects.create(
                        date=row[0],
                        old_testament=row[1],
                        new_testament=row[2],
                        psalm=row[3]
                    )

            self.stdout.write(self.style.SUCCESS("Successfully imported reading plan!"))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error: {e}"))
