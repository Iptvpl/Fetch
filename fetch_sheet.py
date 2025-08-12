import requests
import csv
from io import StringIO

sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTpBTvSmJZDwmmFtxg8wXpPZIqu1_VbXiZzXnFUv1LSNWmaz69R9RceGR4OboLmeZ-aa46lIHZ8OfmQ/pub?gid=0&single=true&output=csv"

response = requests.get(sheet_url)
response.raise_for_status()

data = StringIO(response.text)
reader = csv.reader(data)

output_lines = []

for row in reader:
    # Make sure row has at least columns A and B
    val_a = row[0] if len(row) > 0 else ""
    val_b = row[1] if len(row) > 1 else ""
    
    output_lines.append(val_a)
    output_lines.append(val_b)

with open("output.txt", "w", encoding="utf-8") as f:
    for line in output_lines:
        f.write(line + "\n")
