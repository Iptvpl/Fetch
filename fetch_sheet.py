import requests
import csv
from io import StringIO

sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTpBTvSmJZDwmmFtxg8wXpPZIqu1_VbXiZzXnFUv1LSNWmaz69R9RceGR4OboLmeZ-aa46lIHZ8OfmQ/pub?output=csv"

response = requests.get(sheet_url)
response.raise_for_status()

data = StringIO(response.text)
reader = csv.reader(data)

target_value = None

for i, row in enumerate(reader):
    if i == 1:  # 2nd row
        if len(row) > 2:  # check 3rd column exists
            target_value = row[2]
        else:
            print(f"Row {i+1} does not have 3 columns: {row}")
        break

if target_value is None:
    print("Warning: target_value not found in sheet. Setting default empty string.")
    target_value = ""

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(target_value + "\n")
