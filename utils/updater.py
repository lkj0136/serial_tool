import requests

def check_for_updates(current_version):
    response = requests.get("https://example.com/version")
    latest_version = response.text
    return latest_version > current_version

def download_update():
    response = requests.get("https://example.com/update", stream=True)
    with open("update.zip", "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
