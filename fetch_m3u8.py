import requests
import re

def fetch_m3u8_link():
    url = "http://tv.basnetbd.com/player.php?stream=18"
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to get page")
        return None

    match = re.search(r'(http[^\'"\s]+\.m3u8\?token=[^\'"\s]+)', response.text)
    if match:
        return match.group(1)
    else:
        print("No m3u8 link found")
        return None

if __name__ == "__main__":
    link = fetch_m3u8_link()
    if link:
        print(f"Fresh m3u8 link: {link}")
    else:
        print("Failed to fetch link")
