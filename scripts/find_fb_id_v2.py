import requests
import re

def find_ids():
    url = "https://www.facebook.com/taximlv"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        r = requests.get(url, headers=headers)
        # Find all long numbers
        ids = re.findall(r'"pageID":"(\d+)"', r.text)
        ids += re.findall(r'"delegate_page_id":"(\d+)"', r.text)
        ids += re.findall(r'"id":"(\d+)"', r.text)
        # Also look for any 15 digit numbers that might be IDs
        ids += re.findall(r'[^\d](\d{15})[^\d]', r.text)
        
        unique_ids = list(set(ids))
        print(f"FOUND IDS: {unique_ids}")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    find_ids()
