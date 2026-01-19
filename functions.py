import requests
headers = {
    "User-Agent": "Mozilla/5.0"
}


def save_image(url):
    image = requests.get(url, timeout=15, headers=headers)
    image.raise_for_status()
    with open("file.jpg", "wb") as file:
        file.write(image.content)
    return "file.jpg"
