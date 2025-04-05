""" 
File Download Automation
A script that allows bulk downloading of files from the internet based on a list of URLs. 
This is especially useful for data analysis tasks, dataset collection, or automating repetitive download tasks. 
"""

""" 
Note!
Before running the script, you need to install the requests library.
You can do this by running the following command in your terminal or command prompt
-- pip install requests -- 
"""

import os
import requests

# Ścieżka do pliku z URL-ami (każdy URL w nowej linii)
URL_LIST_FILE = "urls.txt"

# Folder do zapisu pobranych plików
DOWNLOAD_DIR = "downloads"

# Tworzymy folder, jeśli nie istnieje
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def download_file(url, save_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        # Pobieramy nazwę pliku z URL-a
        filename = url.split("/")[-1] or "downloaded_file"
        full_path = os.path.join(save_path, filename)

        with open(full_path, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Downloaded: {filename}")
    except Exception as e:
        print(f"Failed to download from {url}: {e}")

def main():
    if not os.path.isfile(URL_LIST_FILE):
        print(f"URL list file not found: {URL_LIST_FILE}")
        return

    with open(URL_LIST_FILE, "r") as f:
        urls = [line.strip() for line in f if line.strip()]

    print(f"Found {len(urls)} URLs to download.\n")

    for url in urls:
        download_file(url, DOWNLOAD_DIR)

if __name__ == "__main__":
    main()