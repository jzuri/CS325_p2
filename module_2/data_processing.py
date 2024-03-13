import requests
from bs4 import BeautifulSoup

def scrape_article(url):
    """Scrape article content from a given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        article_content = soup.find('div', class_='showBlogPage')
        if article_content:
            return article_content.get_text(separator='\n')
        else:
            return "Just go ahead and change your major =P"
    except requests.exceptions.RequestException as e:
        print("Error fetching URL.")
        return None

