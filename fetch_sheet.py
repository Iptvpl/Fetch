import requests
import csv
from io import StringIO

# Google Sheet CSV link
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTpBTvSmJZDwmmFtxg8wXpPZIqu1_VbXiZzXnFUv1LSNWmaz69R9RceGR4OboLmeZ-aa46lIHZ8OfmQ/pub?output=csv"

# Download CSV
response = requests.get(sheet_url)
data = StringIO(response.text)
reader = csv.reader(data)

# Example: get text from row 2, column 3
for i, row in enumerate(reader):
    if i == 1:  # 2nd row (index 1)
        print(row[2])  # 3rd column
