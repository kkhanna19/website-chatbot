import requests
from bs4 import BeautifulSoup

def crawl_website(url: str) -> str:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["script", "style", "header", "footer", "nav", "aside"]):
        tag.decompose()

    text = soup.get_text(separator=" ")
    return " ".join(text.split())
