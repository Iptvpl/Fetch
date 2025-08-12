import requests
import csv
from io import StringIO

# Google Sheet CSV link
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTpBTvSmJZDwmmFtxg8wXpPZIqu1_VbXiZzXnFUv1LSNWmaz69R9RceGR4OboLmeZ-aa46lIHZ8OfmQ/pub?output=csv"

# Download the sheet as CSV
response = requests.get(sheet_url)
response.raise_for_status()

# Parse CSV
data = StringIO(response.text)
reader = csv.reader(data)

# Example: get cell from Row 2, Column 3
for i, row in enumerate(reader):
    if i == 1:  # Second row
        target_value = row[2]  # Third column
        break

# Save to file
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(target_value + "\n")
