import csv

def write_csv_date(data, filename):
    with open('bible_reading_plan.xlsx', mode='w', newline='') as csv_file:
        plan_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        plan_writer.writerow(data[0].keys())
        for row in plan_writer:
            plan_writer.writerow(row.values())




        fieldnames = ['date', 'old_testament', 'new_testament', 'psalm']

