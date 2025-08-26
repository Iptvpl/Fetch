import requests
import csv
from io import StringIO
from datetime import datetime, timedelta, timezone

# Google Sheet CSV link
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTpBTvSmJZDwmmFtxg8wXpPZIqu1_VbXiZzXnFUv1LSNWmaz69R9RceGR4OboLmeZ-aa46lIHZ8OfmQ/pub?output=csv"

# Fetch CSV from Google Sheets
response = requests.get(sheet_url)
response.raise_for_status()

data = StringIO(response.text)
reader = csv.reader(data)

# Prepare M3U playlist lines
output_lines = ["#EXTM3U"]  # M3U header

# Skip header row if present (optional)
next(reader, None)

for row in reader:
    if len(row) >= 2:
        channel_name = row[0].strip()
        stream_url = row[1].strip()

        if channel_name and stream_url:
            output_lines.append(f"#EXTINF:-1,{channel_name}")
            output_lines.append(stream_url)

# Save playlist file
with open("output.m3u", "w", encoding="utf-8") as f:
    f.write("\n".join(output_lines))

# --- Logging Section ---
# Get current time in GMT+6 (12-hour format without offset)
gmt_plus6 = timezone(timedelta(hours=6))
run_time = datetime.now(gmt_plus6).strftime("%Y-%m-%d %I:%M:%S %p")

log_entry = f"Script run at {run_time}\n"

# Append log entry to log.txt
with open("log.txt", "a", encoding="utf-8") as log_file:
    log_file.write(log_entry)

print("✅ Playlist generated and log updated.")
