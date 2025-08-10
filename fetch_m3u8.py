import requests
import re
import sys

def fetch_m3u8_link():
    url = "http://tv.basnetbd.com/player.php?stream=18"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching page: {e}")
        sys.exit(1)

    match = re.search(r'(http[^\'"\s]+\.m3u8\?token=[^\'"\s]+)', response.text)
    if match:
        return match.group(1)
    else:
        print("No m3u8 link found in page.")
        sys.exit(1)

if __name__ == "__main__":
    link = fetch_m3u8_link()
    print(f"Fresh m3u8 link: {link}")
