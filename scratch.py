import requests
from requests_oauthlib import OAuth1

# public key and private key
auth = OAuth1("*******************", "**********************")
endpoint = "https://api.thenounproject.com/v2/icon?query=ultraball"
response = requests.get(endpoint, auth=auth)
responseJSON = response.json()
print(responseJSON)




import csv

def write_csv(data, filename='bible_reading_plan.csv'):
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = ['date', 'old_testament', 'new_testament', 'psalm']
        plan_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        plan_writer.writeheader()
        for row in plan_writer:
            plan_writer.writerow(row)
    


