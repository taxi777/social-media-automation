import requests
import re

def find_page_id():
    url = "https://www.facebook.com/taximlv"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        r = requests.get(url, headers=headers)
        # Try different patterns
        patterns = [
            r'"pageID":"(\d+)"',
            r'"delegate_page_id":"(\d+)"',
            r'"id":"(\d+)"'
        ]
        for pattern in patterns:
            match = re.search(pattern, r.text)
            if match:
                print(f"FOUND: {match.group(1)}")
                return
        print("NOT FOUND")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    find_page_id()
