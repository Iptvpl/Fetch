import requests
import csv
from io import StringIO

sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTpBTvSmJZDwmmFtxg8wXpPZIqu1_VbXiZzXnFUv1LSNWmaz69R9RceGR4OboLmeZ-aa46lIHZ8OfmQ/pub?gid=0&single=true&output=csv"

response = requests.get(sheet_url)
response.raise_for_status()

data = StringIO(response.text)
reader = csv.reader(data)

column_index = 0  # 0 for column A, 1 for B, etc.

all_values = []

for row in reader:
    if len(row) > column_index:
        all_values.append(row[column_index])
    else:
        all_values.append("")  # if column is missing in that row, add empty string

# Save all column data, one value per line
with open("output.txt", "w", encoding="utf-8") as f:
    for value in all_values:
        f.write(value + "\n")
