import requests
import csv
from io import StringIO

sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTpBTvSmJZDwmmFtxg8wXpPZIqu1_VbXiZzXnFUv1LSNWmaz69R9RceGR4OboLmeZ-aa46lIHZ8OfmQ/pub?gid=0&single=true&output=csv"

response = requests.get(sheet_url)
response.raise_for_status()

data = StringIO(response.text)
reader = csv.reader(data)

target_value = ""  # default empty

for i, row in enumerate(reader):
    if i == 0:  # first row
        if len(row) > 0:
            target_value = row[0]
        else:
            print(f"Row {i+1} has no columns.")
        break

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(target_value + "\n")
