import requests
from bs4 import BeautifulSoup

def scrape_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Example: Find all paragraph tags
        paragraphs = soup.find_all('p')
        data = [p.text for p in paragraphs]
        return data
    else:
        return None