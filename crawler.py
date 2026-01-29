import requests
from bs4 import BeautifulSoup


def crawl_website(url):
    """
    Extract meaningful text from a website URL.
    Removes header, footer, nav, ads-like sections.
    """

    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return None, "Website not reachable."

        soup = BeautifulSoup(response.text, "html.parser")

        # Remove irrelevant sections
        for tag in soup(["header", "footer", "nav", "aside", "script", "style"]):
            tag.decompose()

        text = soup.get_text(separator=" ")
        clean_text = " ".join(text.split())

        if len(clean_text) < 200:
            return None, "Website has insufficient text content."

        title = soup.title.string if soup.title else "No Title"

        return {"text": clean_text, "title": title}, None

    except:
        return None, "Invalid or unreachable URL."
