The scratch.py file currently has the code I was working on to write the csv file. It needs some work.


Possible apis:

IQ Bible API: Provides tools to build Bible apps and websites, including original Hebrew and Greek, audio narrations, and study tools. 
https://rapidapi.com/vibrantmiami/api/iq-bible/details (audio narrations!, Original Greek and Hebrew text!, Strongs...)
https://rapidapi.com/vibrantmiami/api/iq-bible
Use for Greek and Hebrew/audio narrations/strongs
name: berlyKay
API key: 1be48f3b0amsh89f3a6162da0e01p1f5bf0jsn8e82688afad6
Example get request for audio: https://iq-bible.p.rapidapi.com/GetAudioNarration?bookId=01&chapterId=02&versionId=kjv
**The GetAudio view is currently configured so that the user will be able to click a play audio button for the day. (They won't be able to enter their choice for Book/Chapter/Verse. I might add that feature later.) 


[Biblegateway.com](https://www.biblegateway.com/api/documentation)
All requests use the base url of:
https://api.biblegateway.com/2/


API.Bible  **This one doesn't have ESV available
Key: 5f08eb4600c041fa7dc003877a6a8f0a
Name: Code Platoon's App
[ Base URL: api.scripture.api.bible ]
https://api.scripture.api.bible/v1/swagger.json
endpoint for chapter: /v1/bibles/{bibleId}/books/{bookId}/chapters




ESV API
https://api.esv.org/account/reading_plan/
Authorization: Token d6ce5b1b49a0f64132ac5667312743e76964fbb1
Be sure to follow copyright restrictions. Incluse ESV on all verses, and have a separate page with:
Scripture quotations are from the ESV® Bible (The Holy Bible, English Standard Version®), © 2001 by Crossway, 
a publishing ministry of Good News Publishers. Used by permission. All rights reserved. The ESV text may not 
be quoted in any publication made available to the public by a Creative Commons license. The ESV may not be 
translated into any other language.


Bible SuperSearch API: A free web service API that allows the Bible SuperSearch Bible search engine to be used on websites or apps. 
https://api.biblesupersearch.com/




The Bible_Reading_plan in the data folder has the data. If I want to be able to read it, I'll need to add one of these:
Using openpyxl:
from openpyxl import load_workbook

# Path to the file
file_path = 'data/bible_reading_plan.xlsx'

# Load the workbook
workbook = load_workbook(filename=file_path)

# Select a sheet by name or index
sheet = workbook.active  # Or workbook['Sheet1']

# Read data from the sheet
for row in sheet.iter_rows(values_only=True):  # Iterate through rows
    print(row)  # Print each row as a tuple


Using pandas
import pandas as pd

# Path to the file
file_path = 'data/bible_reading_plan.xlsx'

# Read the Excel file
df = pd.read_excel(file_path)

# Example: Print the first 5 rows
print(df.head())

# Example: Iterate through rows
for index, row in df.iterrows():
    print(row['Date'], row['New Testament'], row['Old Testament'])

If I'm going to deploy, update settings.py:
import os

# Add a constant for the data folder
DATA_DIR = os.path.join(BASE_DIR, 'data')

...and use something like this in my view or script:
from django.conf import settings
import os
import pandas as pd

# Path to the file
file_path = os.path.join(settings.DATA_DIR, 'bible_reading_plan.xlsx')

# Read the Excel file using pandas
df = pd.read_excel(file_path)

# Example: Print the first few rows
print(df.head())


